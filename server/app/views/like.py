from flask import Blueprint, request, jsonify

from app.modle.modle import db,User,Video

from app.utils.addr_help import Get_network_address

like_blueprint = Blueprint("like", __name__)


@like_blueprint.route("/", methods=["GET", "POST", "DELETE"])
def like():

    if request.method == "GET":
        user_name = request.args.get("user_name")
        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        videos = user.videos
        likes = []
        for video in videos:
            addr = Get_network_address(video.video_addr,video.video_fid)
            video_info = {
                "video_id": video.video_id,
                "video_name": video.video_name,
                "video_addr": addr
            }
            likes.append(video_info)

        return jsonify({"code": 200, "likes": likes})

    # 用户将视频添加到喜欢表中
    elif request.method == "POST":
        user_name = request.form["user_name"]
        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        video_id = request.form["video_id"]
        if not video_id:
            return jsonify({"code": 500, "message": "video_id is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        video = Video.query.filter(Video.video_id==video_id).first()
        if not video:
            return jsonify({"code": 500, "message": "no video"})

        if video not in user.videos:
            user.videos.append(video)
        else:
            return jsonify({"code": 500, "message": "user had liked the video before"})

        # 将video_like值+1
        video.video_like += 1

        # 将tag_like值+1
        tags = video.tags
        for tag in tags:
            tag.tag_like += 1

        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    # 用户讲视频从喜欢表中删除
    elif request.method == "DELETE":
        user_name = request.form["user_name"]
        video_id = request.form["video_id"]
        if not user_name or not video_id:
            return jsonify({"code": 500, "message": "user_name or video_id is empty"})

        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        video = Video.query.filter(Video.video_id==video_id).first()
        if not video:
            return jsonify({"code": 500, "message": "no video"})

        if video in user.videos:
            user.videos.remove(video)
        else:
            return jsonify({"code": 500, "message": "user didnt like the video before"})

        # 将video_like值-1
        video.video_like -= 1

        # 将tag_like值-1
        tags = video.tags
        for tag in tags:
            tag.tag_like -= 1

        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    else:
        return jsonify({"code": 500, "message": "method is not support"})