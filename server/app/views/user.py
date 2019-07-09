import uuid

from flask import Blueprint, request, jsonify

from app.modle.modle import db, User

from app.utils.time_help import expire

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["GET", "POST", "DELETE"])
def user():

    if request.method == "GET":
        user_name = request.args.get("user_name")

        if not user_name:
            return jsonify({"code": 500, "message": "user_name is empty"})

        user = User.query.filter(User.user_name == user_name).first()
        if not user:
            return jsonify({"code": 500, "message": "no user"})

        # 用户存在level_id就查询level_name,level_time
        if user.level:
            behind_days = expire(user.user_expired)
            user_map = {
                "user_name": user.user_name,
                "user_level": user.user_level,
                "level_name": user.level.level_name,
                "level_time": behind_days
            }

        # 用户没有level,就返回空值
        else:
            user_map = {
                "user_name": user.user_name,
                "user_level": "",
                "level_name": "",
                "level_time": ""
        }

        return jsonify({"code": 200, "user_info": user_map})

    elif request.method == "POST":
        user = User()
        user.user_name = str(uuid.uuid1())

        db.session.add(user)
        db.session.commit()

        # 新建用户,直接返回空的level信息
        user_map = {
            "user_name": user.user_name,
            "user_level": "",
            "level_name": "",
            "level_time": ""
        }

        return jsonify({"code": 200, "user_info": user_map})

    else:
        return jsonify({"code": 500, "message": "method is not support"})