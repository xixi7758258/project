from flask import Flask

# create_app create a app.
# @params: <config_object: object>.
# @return: <app: object>.
def create_app(config_object):

    # build flask app.
    app = Flask(__name__)
    
    # app load config object.
    app.config.from_object(config_object)

    # http request oirgin *.
    from flask_cors import CORS
    CORS(app, supports_credentials=True, resources=r"/*")

    # orm modle.
    from app.modle.modle import db
    db.init_app(app)

    # from app.views.admin import admin
    # admin.init_app(app)

    # register views def.
    from app.views.ad import ad_blueprint
    from app.views.level import level_blueprint
    from app.views.order import order_blueprint
    from app.views.pay import pay_blueprint
    from app.views.user import user_blueprint
    from app.views.video import video_blueprint
    from app.views.test import test_blueprint

    app.register_blueprint(ad_blueprint,url_prefix='/ad')
    app.register_blueprint(level_blueprint,url_prefix='/level')
    app.register_blueprint(order_blueprint,url_prefix='/order')
    app.register_blueprint(pay_blueprint,url_prefix='/pay')
    app.register_blueprint(user_blueprint,url_prefix='/user')
    app.register_blueprint(video_blueprint,url_prefix='/video')
    app.register_blueprint(test_blueprint,url_prefix='/test')

    return app
    
