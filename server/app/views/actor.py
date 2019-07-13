from flask import Blueprint , request, jsonify

from app.modle.modle import db, Actor
from app.confs.config import Config
from app.utils.file_help import ObtainFileStorageAddr, UploadFile

actor_blueprint = Blueprint("actor", __name__)

@actor_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def actor():
    
    if request.method == "GET":
        actor_id =  request.args.get("actor_id")
        if actor_id:
            actor = Actor.query.filter_by(actor_id=actor_id).first()
            if not actor:
                return jsonify({"code": 500, "message": "value error"})
            return jsonify({"code": 200, "actor_info":actor.actor_info()})

        actors = Actor.query.all()
        actor_info_list = []
        for actor in actors:
            actor_info_list.append(actor.actor_info())
        return jsonify({"code": 200, "actor_info_list": actor_info_list})

    if request.method == "POST":
        actor_file = request.files["actor"]
        actor_name = str(actor_file.filename)[0:str(actor_file.filename).find(".")]
    
        fid, port = ObtainFileStorageAddr(Config.FLIE_MASTER_URL)
        code = UploadFile(Config.FLIE_SROTAGE_URL[port]["URL"],port,fid,actor_name,actor_file)
        if code != 201:
            return jsonify({"code": 500, "message": "error"})

        actor = Actor()
        actor.actor_name = actor_name
        actor.actor_fid = fid
        actor.actor_addr = port

        db.session.add(actor)
        db.session.commit()
        return jsonify({"code": 200, "message": "success"})

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        pass
    
    return jsonify({"code": 500, "message": "methon error"})


@actor_blueprint.route("/simple", methods=["GET"])
def actor_simple():
    if request.method == "GET":
        actors = Actor.query.all()
        actor_info_list = []
        for actor in actors:
            actor_info_list.append(actor.actor_simple_info())

        return jsonify({"code": 200, "actor_info_list": actor_info_list})