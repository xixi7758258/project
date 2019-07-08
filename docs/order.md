Order CRUD


查询
url: ip:port/order?
method: GET
params: <"all": bool>, <"user_name": str>, <"order_index": str>, <"start_time": str>, <"end_time": str>
return: 
{
    "code": 200,
    "ords": [
        {
            "level": "member",
            "order_index": "49d3c4c6-a134-11e9-a688-acde48001122",
            "order_number": 3,
            "order_time": "2019-07-8 10:55:56",
            "pay_time": "",
            "user": "luodeman"
        },
        ...
    ]
}

增加
url: ip:port/order/
method: POST
params: <"user_name": str>, <"order_number": int>
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}
