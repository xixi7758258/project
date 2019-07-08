from flask import Blueprint,request,jsonify
from app.modle.modle import db,Level,User,Order
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

        #ip:port/order?all=True,查询所有订单
        if all=="True":
            ords = Order.query.all()

        #定义参数列表
        args_list = []
        if user_name:
            user = User.query.filter(User.user_name==user_name).first()
            user_id = user.user_id
            args_list.append("user=" + str(user_id))

        if order_index:
            args_list.append("order_index='" + str(order_index) + "'")

        if start_time:
            args_list.append("order_time>='" + str(start_time)+"'")

        if end_time:
            args_list.append("order_time<='" + str(end_time)+"'")

        #将参数列表组装成sql语句，并执行
        if args_list:
            sql = "select * from `order` where " + " and ".join(args_list) + ";"
            ords = db.session.execute(sql)

        ords_list = []
        for ord in ords:
            #如果没有user_name,就去user表获取
            if not user_name:
                user = User.query.filter(User.user_id==ord.user).first()
                user_name = user.user_name

            #在level表获取level_name()
            level = Level.query.filter(Level.level_id==ord.level).first()
            level_name = level.level_name

            #初始化订单创建时间和支付时间，如果数据库中存在时间就赋值
            order_time = ""
            pay_time = ""
            if ord.order_time:
                order_time = datetime.datetime.strftime(ord.order_time,"%Y-%m-%-d %H:%M:%S")
            if ord.pay_time:
                pay_time = datetime.datetime.strftime(ord.pay_time,"%Y-%m-%-d %H:%M:%S")

            #组建返回值
            ord_map = {"order_index":ord.order_index,"order_time":order_time,"pay_time":pay_time,"order_number":ord.order_number,"user":user_name,"level":level_name}
            ords_list.append(ord_map)

        return jsonify({"code": 200, "ords": ords_list})

    elif request.method == "POST":
        user_name = request.form["user_name"]
        order_number = request.form["order_number"]

        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        user_id = user.user_id
        level_id = user.user_level

        ord = Order()
        ord.user = user_id
        ord.level = level_id
        ord.order_number = order_number
        ord.order_index = datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S%f") +  "-" + user_name

        db.session.add(ord)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    else:
        return jsonify({"code": 500, "message": "method is not support"})