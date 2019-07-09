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

    # register views def.
    from app.views import ad, pay, tag, actor, level, order, user, video, like, search, test

    app.register_blueprint(ad.ad_blueprint,url_prefix='/ad')
    app.register_blueprint(pay.pay_blueprint,url_prefix='/pay')
    app.register_blueprint(tag.tag_blueprint,url_prefix='/tag')
    app.register_blueprint(user.user_blueprint,url_prefix='/user')
    app.register_blueprint(like.like_blueprint,url_prefix='/like')
    app.register_blueprint(actor.actor_blueprint,url_prefix='/actor')
    app.register_blueprint(order.order_blueprint,url_prefix='/order')
    app.register_blueprint(level.level_blueprint,url_prefix='/level')
    app.register_blueprint(video.video_blueprint,url_prefix='/video')
    app.register_blueprint(search.search_blueprint,url_prefix='/search')
    
    app.register_blueprint(test.test_blueprint,url_prefix='/test')

    return app
    
