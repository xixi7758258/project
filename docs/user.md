Video CRUD

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