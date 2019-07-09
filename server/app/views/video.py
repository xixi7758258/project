from flask import Blueprint, request, jsonify

from app.modle.modle import Video


video_blueprint = Blueprint("video", __name__)

# video crud.
@video_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])

    if request.method == "GET":
        videos = Video.query.filter_by(video_ative=True).all()
        for video in videos:
            pass
        return

    if request.method == "POST":
        
        return
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":
        
        return
    
    return jsonify({"code": 500, "message": "method error"})