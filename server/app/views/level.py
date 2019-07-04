from flask import Blueprint

level_blueprint = Blueprint("level", __name__)

@level_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def level():
    if request.method == "GET":
        levels = Level.query.all()
        if not levels:
            return jsonify({"code": 200, "message": "level is null"})
        else:
            l_list = []
            for l in levels:
                l_map = {"level_id": l.level_id, "level_name": l.level_name, "level_price": l.level_price,
                         "level_time": l.level_time, "level_active": l.level_active}
                l_list.append(l_map)

            return jsonify({"code": 200, "levels": l_list})

    elif request.method == "POST":
        level_name = request.form["level_name"]
        level_price = request.form["level_prive"]
        level_time = request.form["level_time"]

        l = Level()

        l.level_name = level_name
        l.level_price = level_price
        l.level_time = level_time

        db.session.add(l)
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
        pass

    else:
        return jsonify({"code": 500, "message": "method is not support"})