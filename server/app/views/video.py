from flask import Blueprint ,request, jsonify
from app.modle.modle import db, Tag

video_blueprint = Blueprint("video", __name__)

# Tag CRUD.
@video_blueprint.route("/tag", methods=["GET", "POST", "PUT", "DELETE"])
def tag():
    
    # 获取所有tag.
    if request.method == "GET":
        tag_list = []
        tags = Tag.query.all()
        for tag in tags:
            tag_map = {"tag_id": tag.tag_id, "tag_name":tag.tag_name}
            tag_list.append(tag_map)
        return jsonify({"code": 200, "tags": tag_list})

    # 创建新的tag.
    if request.method == "POST":

        tag_name = request.form["tag_name"]
        if tag_name == "":
            return  jsonify({"code": 500, "message": "tag_name empty"})

        new_tag = Tag()
        new_tag.tag_name = tag_name

        db.session.add(new_tag)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    # 修改tag名.
    if request.method == "PUT":
        tag_id = request.form["tag_id"]
        tag_name = request.form["tag_name"]
        if not int(tag_id) or tag_name == "":
            return jsonify({"code": 500, "message": "tag_id empty"})

        result = Tag.query.filter(Tag.tag_id==tag_id).first()
        result.tag_name = tag_name
        db.session.commit()
        return jsonify({"code":200, "message": "ok"})

    # 删除指定tag.
    if request.method == "DELETE":
        tag_id = request.form["tag_id"]
        if not int(tag_id):
            return jsonify({"code":500, "message": "tag_id empty"})

        result = Tag.query.filter(Tag.tag_id==tag_id).first()
        db.session.delete(result)
        db.session.commit()
        return jsonify({"code":200, "message": "ok"})
    
    return jsonify({"code":500, "message": "mothod error"})