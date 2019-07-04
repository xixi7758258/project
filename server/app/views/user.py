from flask import Blueprint,request,jsonify
from app.modle.modle import db,User,Video,

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/like", methods=["GET","POST","DELETE"])
def like():

    if request.method == "GET":
        user_id = request.form["user_id"]
        if not user_id:
            return jsonify({"code":500, "message": "user_id is empty"})
        
        user = User.query.filter(User.user_id=user_id).first()
        vs = user.video
        likes = []

        for v in vs:
            v_map = {"video_id":v.video_id,"video_name":v.video_name,"video_addr":v.video_addr}
            videos.append(v_map)

        return jsonify({"code": 200, "likes": likes})

    #用户将视频添加到喜欢表中
    elif request.method == "POST":
        user_id = request.form["user_id"]
        video_id = request.form["video_id"]
        if not user_id or not video_id:
            return jsonify({"code":500, "message": "user_id or video_id is empty"})
        
        user = User.query.filter(User.user_id=user_id).first()
        video = Video.query.filter(Video.video_id=video.id).first()
        user.video.append(video)
        
        db.session.add(user)
        db.session.commit()

        return jsonify({"code":200, "message": "ok"})

    #用户讲视频从喜欢表中删除
    elif request.method == "DELETE":
        user_id = request.form["user_id"]
        video_id = request.form["video_id"]
        if not user_id or not video_id:
            return jsonify({"code":500, "message": "user_id or video_id is empty"})
        
        user = User.query.filter(User.user_id=user_id).first()
        video = Video.query.filter(Video.video_id=video.id).first()
        user.video.remove(video)

        db.session.commit()

        return jsonify({"code":200, "message": "ok"})
    
    else:
        return  jsonify({"code": 500, "message": "method is not support"})