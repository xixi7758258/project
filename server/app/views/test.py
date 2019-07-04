from flask import Blueprint

test_blueprint = Blueprint("test", __name__)

from app.modle.modle import db,User,Level

@test_blueprint.route("/create")
def create():
    db.create_all()
    return "创建成功"

@test_blueprint.route("/drop")
def drop():
    db.drop_all()
    return "删除成功"

@test_blueprint.route("/add")
def add():
    l = Level(level_name='vip')
    db.session.add(l)
    db.session.commit()
    u = User(user_name="xixi",user_level=1)
    db.session.add(l)
    db.session.add(u)
    db.session.commit()
    return "添加成功"

@test_blueprint.route("/select")
def select():
    a = User.query.all()
    return a[0].user_name