from flask import Flask


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from app.views.ad import ad_blueprint
    from app.views.level import level_blueprint
    from app.views.order import order_blueprint
    from app.views.pay import pay_blueprint
    from app.views.user import user_blueprint
    from app.views.video import video_blueprint

    app.register_blueprint(ad_blueprint,url_prefix='/ad')
    app.register_blueprint(level_blueprint,url_prefix='/level')
    app.register_blueprint(order_blueprint,url_prefix='/order')
    app.register_blueprint(pay_blueprint,url_prefix='/pay')
    app.register_blueprint(user_blueprint,url_prefix='/user')
    app.register_blueprint(video_blueprint,url_prefix='/video')

    return app
    
