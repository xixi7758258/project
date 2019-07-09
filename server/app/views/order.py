import datetime

from flask import Blueprint, request, jsonify

from app.modle.modle import db, User, Order

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
            orders = Order.query.all()
        else:
            # 根据用户名查
            if user_name:
                user = User.query.filter(User.user_name == user_name).first()
                if user:
                    orders = user.order
                else:
                    return jsonify({"code": 500, "message": "no user"})

            # 根据单号查询
            elif order_index:
                orders = Order.query.filter(Order.order_index == order_index).all()

            #根据开始时间
            elif start_time and not end_time:
                start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                orders = Order.query.filter(Order.create_time >= start_time).all()

            #根据结束时间
            elif end_time and not start_time:
                end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                orders = Order.query.filter(Order.create_time <= end_time).all()

            #根据开始和结束时间
            elif end_time and start_time:
                start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                orders = Order.query.filter(Order.create_time >= start_time, Order.create_time <= end_time).all()

            else:
                return jsonify({"code": 500, "message": "args is not support"})

        order_info_list = []
        if orders:
            for order in orders:
                order_info_list.append(order.order_info())

        return jsonify({"code": 200, "orders": order_info_list})


    elif request.method == "POST":
        user_name = request.form["user_name"]
        order_number = request.form["order_number"]

        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        order = Order()
        order.user = user.user_id
        order.level = user.user_level
        order.order_number = order_number
        order.order_index = datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S%f") +  "-" + user_name

        db.session.add(order)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    else:
        return jsonify({"code": 500, "message": "method is not support"})