Tag CRUD

查询
url: ip:port/video/tag
method: GET
params: 
return: {"code": 200, "tags": [{"tag_id": "xxx", "tag_name": "xxx"}, ... ...]}

增加
url: ip:port/video/tag
method: POST
params: <"tag_name": "xxx">
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}

修改
url: ip:port/video/tag
method: PUT
params: <"tag_id": "xxx">
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}

删除
url: ip:port/video/tag
method: DELETE
params: <"tag_id": "xxx">
retuen: {"code": 200, "message": "OK"} / {"code": 500, "message": "error"}