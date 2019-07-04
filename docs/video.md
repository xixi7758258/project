Video CRUD

查询
url: ip:port/video/
method: GET
params: 
return: 
    {
        "code": 200,
        "videos": [
            {
                "tags": [{"tag_id": xx, "tag_name": "xx"},..],
                "video_addr": "xx",
                "video_desc": "xx",
                "video_id": xx,
                "video_like": xx,
                "video_name": "xx"
            },
            ... ...
        ]
    }

增加
url: ip:port/video/
method: POST
params: <"video_name": "xxx">, <"video_desc": "xxxx">, <"video": file>, <"tags":[x,x,x,x]>
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}

修改
url: ip:port/video/
method: PUT
params: 
retuen: 

删除
url: ip:port/video/
method: DELETE
params: <"video": "xxx">
retuen: {"code": 200, "message": "OK"}