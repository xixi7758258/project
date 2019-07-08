from flask import Blueprint,request,jsonify
from app.modle.modle import db,User,Order
import datetime

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/",methods=["GET", "POST", "PUT", "DELETE"])
def order():
    if request.method == "GET":
        all = request.args.get("all")
        user_name = request.args.get("user_name")
        order_index = request.args.get("order_index")
        start_time = request.args.get("start_time")
        end_time = request.args.get("end_time")

        #全查询
        if all=="True":
            ords = Order.query.all()
        else:
            # 根据用户名查
            if user_name:
                user = User.query.filter(User.user_name == user_name).first()
                if user:
                    ords = user.order
                else:
                    return jsonify({"code": 500, "message": "no user"})

            # 根据单号查询
            elif order_index:
                ords = Order.query.filter(Order.order_index == order_index).all()

            #根据开始时间
            elif start_time and not end_time:
                start_time = datetime.datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
                ords = Order.query.filter(Order.create_time >= start_time).all()

            #根据结束时间
            elif end_time and not start_time:
                end_time = datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
                ords = Order.query.filter(Order.create_time <= end_time).all()

            #根据开始和结束时间
            elif end_time and start_time:
                start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                ords = Order.query.filter(Order.create_time >= start_time, Order.create_time <= end_time).all()
            else:
                return jsonify({"code": 500, "message": "args is not support"})

        ord_list = []
        if ords:
            for ord in ords:
                ord_list.append(ord.info())

        return jsonify({"code": 200, "orders": ord_list})


    elif request.method == "POST":
        user_name = request.form["user_name"]
        order_number = request.form["order_number"]
        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        ord = Order()
        ord.user = user.user_id
        ord.level = user.user_level
        ord.order_number = order_number
        ord.order_index = datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S%f") +  "-" + user_name

        db.session.add(ord)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    else:
        return jsonify({"code": 500, "message": "method is not support"})