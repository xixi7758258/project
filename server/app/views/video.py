from flask import Blueprint ,request, jsonify
from app.modle.modle import db, Tag, Video
from app.utils.file_help import ObtainFileStorageAddr, UploadFile, DeleteFile
from app.confs.config import Config

video_blueprint = Blueprint("video", __name__)

# Video CRUD.
@video_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def video():
    if request.method == "GET":
        vis = []
        vs = Video.query.all()
        for v in vs:
            addr = Config.FLIE_SROTAGE_URL[v.video_addr]["URL"] + ":" + v.video_addr + "/" +v.video_fid
            tis = []
            for tag in v.tags:
                ti = {"tag_id": tag.tag_id, "tag_name": tag.tag_name}
                tis.append(ti)
            vi = {"video_id":v.video_id,"video_name":v.video_name,\
                "video_desc":v.video_desc,"video_addr": addr, "video_like": v.video_like, "tags":tis}
            vis.append(vi)

        return jsonify({"code": 200, "videos": vis})


    if request.method == "POST":
        tags = request.form.getlist("tags")
        video_name = request.form["video_name"]
        video_desc = request.form["video_desc"]
        if video_name == "":
            jsonify({"code": 500, "message": "video_name empty"})

        video = request.files["video"]
        if not video_name:
            jsonify({"code": 500, "message": "video empty"})

        fid, url = ObtainFileStorageAddr(Config.FLIE_MASTER_URL)
        if fid == "":
            jsonify({"code": 500, "message": "fid empty"})
    
        # 存储视频;
        port = url[-4:]
        storage_url = Config.FLIE_SROTAGE_URL[port]["URL"] + ":" + port
        ok = UploadFile(storage_url, fid, video_name, video)

        # 存储信息;
        video_info = Video()
        video_info.video_name = video_name
        video_info.video_addr = port
        video_info.video_fid = fid
        video_info.video_desc = video_desc
        for t_id in tags:
            video_info.tags.append(Tag.query.filter(Tag.tag_id==t_id).first())
        db.session.add(video_info)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        video_id = request.form["video_id"]
        if not int(video_id):
            return jsonify({"code":500, "message": "video_id empty"})

        result = Video.query.filter(Video.video_id==video_id).first()
        storage_url = Config.FLIE_SROTAGE_URL[result.video_addr]["URL"] + ":" + result.video_addr
        DeleteFile(storage_url, result.video_fid)
        db.session.delete(result)
        db.session.commit()
        return jsonify({"code":200, "message": "ok"})

    return jsonify({"code":500, "message": "mothod error"})


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


# Video Search.
@video_blueprint.route("/search", methods=["GET", "POST", "PUT", "DELETE"])
def search():
    if request.method == "GET":
        pass

    if request.method == "POST":
        tags = request.form_list["tag"]
        pass

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        pass

    return jsonify({"code":500, "message": "mothod error"})