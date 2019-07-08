Level CRUD

查询
url: ip:port/level/
method: GET
params: 
return: 
    {
    "code": 200,
    "levels": [
        {
            "level_active": false,
            "level_id": 1,
            "level_name": "vip",
            "level_price": null,
            "level_time": null
        },
        {
            "level_active": true,
            "level_id": 2,
            "level_name": "member",
            "level_price": 99,
            "level_time": 30
        }
    ]
}

增加
url: ip:port/level/
method: POST
params: <"level_name": str>, <"level_price": int>, <"level_time": int>
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}

修改
url: ip:port/level/
method: PUT
params: <"level_id": int>
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}
