from flask import Blueprint, request, jsonify

from app.modle.modle import Video
from app.confs.config import Config
from app.utils.file_help import ObtainFileStorageAddr, UploadFile

video_blueprint = Blueprint("video", __name__)

# video crud.
@video_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def video():
    # 获取单个视频的完整信息或获取所有视频的封面列表;
    if request.method == "GET":

        # 获取单个视频信息.
        video_id = request.args.get("video_id", type=int)
        if video_id:
            video = Video.query.filter_by(video_id=video_id, video_active=True).first()
            # 没有查询到该视频.
            if not video:
                return jsonify({"code": 500, "message": "not found video info"})

            return jsonify({"code": 200, "video_info": video.video_info()})

        # 获取的视频下标页.
        page_idx = request.args.get("page_idx", type=int)

        # 获取视频播放列表.
        result = Video.query.filter_by(video_ative=True).\
            paginate(page_idx if page_idx else 1, Config.Page_Size)
 
        video_cover_list = []
        for video in result.items:
            video_cover_list.append(video.video_cover_list())

        return jsonify({"code": 200, "video_cover_list": video_cover_list, \
            "page_num": result.pages, "page_idx": result.page, "prev": result.has_prev, \
                "next": result.has_next, "total": result.total})


    # 上传视频.
    if request.method == "POST":
        # 获取数据.

        # 文件存入服务器.

        # 信息存入数据库.

        return jsonify({"code": 200, "massage": "success"})
    

    # 修改视频.
    if request.method == "PUT":
        
        return
    

    # 下架视频.
    if request.method == "DELETE":
        
        return

    return jsonify({"code": 500, "message": "method error"})
