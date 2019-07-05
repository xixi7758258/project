User CRUD

查询
url: ip:port/user/like
method: GET
params: user_id
return: 
    {
        "code": 200,
        "likes": [
            {
                "video_addr": "xx",
                "video_id": xx,
                "video_name": "xx"
            },
            ... ...
        ]
    }

增加
url: ip:port/user/like
method: POST
params: <"video_id": "xxx">, <"user_id": "xxxx">
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "user_id or video_id is empty"}


删除
url: ip:port/user/like
method: DELETE
params: <"video_id": "xxx">, <"user_id": "xxxx">
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "user_id or video_id is empty"}

查询用户信息
url: ip:port/user
method: GET
params: user_name
return: {"code": 200, "likes": []} / {"code": 500, "message": "xxx"}
{
    "code": 200,
    "likes": [
        {
            "video_addr": "xxx",
            "video_id": 1,
            "video_name": "诱惑"
        },
        ...
    ]
}

创建
url: ip:port/user
method: POST
params: 
return: {"code": 200, "likes": []} / {"code": 500, "message": "xxx"}
{
    "code": 200,
    "user_info": {
        "level_name": "",
        "level_time": "",
        "user_level": "",
        "user_name": "9015e0c0-9f1a-11e9-8700-acde48001122"
    }
}