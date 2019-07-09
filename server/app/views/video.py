from flask import Blueprint, request, jsonify

from app.modle.modle import Video


video_blueprint = Blueprint("video", __name__)

# video crud.
@video_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def video():
    # 获取单个视频的完整信息或获取所有视频的封面列表;
    if request.method == "GET":

        # 获取单个视频信息.
        video_id = request.args.get("video_id")
        if video_id:
            video = Video.query.filter_by(video_id=video_id).first()
            # 没有查询到该视频.
            if not video:
                return jsonify({"code": 500, "message": "not found video info"})

        return jsonify({"code": 200, "video_info": video.video_info()})

        # 获取视频播放列表.
        videos = Video.query.filter_by(video_ative=True).all()

        # 封装视频信息列表.
        video_cover_list = []
        for video in videos:
            # 调用类方法获取视频封面列表.
            video_cover = video.video_cover_list()
            # 组装进 video_cover_list.
            video_cover_list.append(video_cover)

        return jsonify({"code": 200, "video_cover_list": video_cover_list})

    # 上传视频.
    if request.method == "POST":
        
        return
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":
        
        return
    
    return jsonify({"code": 500, "message": "method error"})
