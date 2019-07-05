from flask import Blueprint,request,jsonify
from app.modle.modle import db,User,Video,Level
import uuid

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/like", methods=["GET","POST","DELETE"])
def like():

    if request.method == "GET":
        user_id = request.form["user_name"]
        if not user_id:
            return jsonify({"code":500, "message": "user_id is empty"})
        
        user = User.query.filter_by(user_name=user_name).first()
        vs = user.video
        likes = []

        for v in vs:
            v_map = {"video_id":v.video_id,"video_name":v.video_name,"video_addr":v.video_addr}
            likes.append(v_map)

        return jsonify({"code": 200, "likes": likes})

    #用户将视频添加到喜欢表中
    elif request.method == "POST":
        user_id = request.form["user_id"]
        video_id = request.form["video_id"]
        if not user_id or not video_id:
            return jsonify({"code":500, "message": "user_id or video_id is empty"})
        
        user = User.query.filter_by(user_id=user_id).first()
        video = Video.query.filter_by(video_id=video.id).first()
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
        
        user = User.query.filter_by(user_id=user_id).first()
        video = Video.query.filter_by(video_id=video.id).first()
        user.video.remove(video)

        db.session.commit()

        return jsonify({"code":200, "message": "ok"})
    
    else:
        return  jsonify({"code": 500, "message": "method is not support"})


@user_blueprint.route("/", methods=["GET","POST","DELETE"])
def user():

    if request.method == "GET":
        user_name = request.args.get("user_name")
        if not user_name:
            return jsonify({"code":500, "message": "user_name is empty"})
        #查询用户，并获取level_id
        user = User.query.filter(User.user_name==user_name).first()
        if not user:
            return jsonify({"code":500, "message": "no user"})
        user_level_id = user.user_level

        l = []
        #用户存在level_id就查询level_name,level_time
        if user_level_id:
            level = Level.query.filter(Level.level_id==user_level_id).first()
            levle_time =  level.level_time
            user_map = {"user_name":user.user_name,"user_level":user_level_id,"level_name":level.level_name,"level_time":levle_time}
            l.append(user_map)      
        #用户没有level,就返回空值
        else:
            user_map = {"user_name":user.user_name,"user_level":"","level_name":"","level_time":""}

        return jsonify({"code":200, "user_info": user_map})
    
    elif request.method == "POST":
        user = User()
        user.user_name = str(uuid.uuid1())
        
        db.session.add(user)
        db.session.commit()
        #新建用户,直接返回空的level信息
        user_map = {"user_name":user.user_name,"user_level":"","level_name":"","level_time":""}
        return jsonify({"code":200, "user_info": user_map})

    else:
        return  jsonify({"code": 500, "message": "method is not support"})