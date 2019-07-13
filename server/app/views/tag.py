from flask import Blueprint ,request, jsonify

from app.modle.modle import db, Tag

tag_blueprint = Blueprint("tag", __name__)


# tag crud.
@tag_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def tag():
    if request.method == "GET":
        tags = Tag.query.all()

        tag_info_list = []
        for tag in tags:
            tag_info = {"tag_id": tag.tag_id, "tag_name": tag.tag_name, "tag_like": tag.tag_like}
            tag_info_list.append(tag_info)

        return jsonify({"code": 200, "tag_info_list": tag_info_list})

    if request.method == "POST":
        tag_info = request.get_json()

        if not tag_info["tag_name"] or Tag.query.filter_by(tag_name=tag_info["tag_name"]):
            return jsonify({"code": 500, "message": "value error"})

        tag = Tag()
        tag.tag_name = tag_info["tag_name"]
        db.session.add(tag)
        db.session.commit()

        return jsonify({"code": 200, "message": "success"})
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":

        return
    
    return jsonify({"code": 500, "message": "method error"})