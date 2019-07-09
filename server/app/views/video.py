from flask import Blueprint, request, jsonify

from app.modle.modle import Video


video_blueprint = Blueprint("video", __name__)


# video crud.
@video_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def video():
    if request.method == "GET":
        
        # 获取单个视频地址.
        video_id = request.args_get("video_id")
        if video_id:
            return jsonify()

        # 获取视频播放列表.
        videos = Video.query.filter_by(video_ative=True).all()

        # 封装视频信息列表.
        video_info_list = []
        for video in videos:
            video_info = {

            }
            video_info_list.append(video_info)

        return jsonify({"code": 200, "video_info_list": video_info_list})

    if request.method == "POST":
        
        return
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":
        
        return
    
    return jsonify({"code": 500, "message": "method error"})
