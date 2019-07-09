from flask import Blueprint, request, jsonify

from app.modle.modle import db, Level

level_blueprint = Blueprint("level", __name__)


@level_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def level():

    if request.method == "GET":
        levels = Level.query.all()

        if not levels:
            return jsonify({"code": 200, "message": "level is null"})
        else:
            level_info_list = []
            for level in levels:
                level_info_list.append(level.level_info())

            return jsonify({"code": 200, "levels": level_info_list})

    elif request.method == "POST":
        level_name = request.form["level_name"]
        level_price = request.form["level_price"]
        level_time = request.form["level_time"]

        level = Level()

        level.level_name = level_name
        level.level_price = level_price
        level.level_time = level_time

        db.session.add(level)
        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    elif request.method == "PUT":
        level_id = request.form["level_id"]
        level = Level.query.filter(Level.level_id == level_id).first()

        if level.level_active:
            level.level_active = False
        else:
            level.level_active = True

        db.session.commit()

        return jsonify({"code": 200, "message": "ok"})

    elif request.method == "DELETE":
        return jsonify({"code": 500, "message": "method is not support"})

    else:
        return jsonify({"code": 500, "message": "method is not support"})