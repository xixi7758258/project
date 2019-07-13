import datetime

from flask_sqlalchemy import SQLAlchemy

from app.utils.addr_help import Get_network_address

db = SQLAlchemy()

# 创建中间表用户与喜好关联
like = db.Table(
    'like',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('video_id', db.Integer, db.ForeignKey('video.video_id'), primary_key=True)
)

# 创建中间表视频与标签关联
video_tag = db.Table(
    'video_tag',
    db.Column('video_id', db.Integer, db.ForeignKey('video.video_id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.tag_id'), primary_key=True)
)


class Video(db.Model):
    # 视频ID，唯一主键
    video_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 演员
    video_actor = db.Column(db.Integer, db.ForeignKey('actor.actor_id'))
    # 番号
    video_idx = db.Column(db.String(64))
    # 名称
    video_name = db.Column(db.String(24))
    # 封面图片地址
    video_img_adr = db.Column(db.String(24))
    # 封面图片密钥
    video_img_fid = db.Column(db.String(24))
    # 简介
    video_desc = db.Column(db.String(64))
    # 地址
    video_addr = db.Column(db.String(24))
    # 密匙
    video_fid = db.Column(db.String(24))
    # 喜欢
    video_like = db.Column(db.Integer, default=0)
    # 视频观看
    video_view = db.Column(db.Integer)
    # 创建时间
    video_ctime = db.Column(db.DateTime)
    # 激活状态
    video_ative = db.Column(db.Boolean, default=True)
    # 创建于用户的关联
    users = db.relationship('User', backref='video', secondary=like)
    # 创建video与tag的关联
    tags = db.relationship('Tag', backref='video', secondary=video_tag)
    # 创建video与actor的关联
    actors = db.relationship('Actor', backref='video')

    def video_info(self):
        return {
            "video_id": self.video_id,
            "video_idx": self.video_idx,
            "video_addr": Get_network_address(self.video_add, self.video_fid),
            "video_name": self.video_name,
            "video_like": self.video_like,
            "video_view": self.video_view,
            "video_actors": self.actors.actor_name,
            "video_ative": self.video_ative,
        }

    def video_cover_list(self):
        return {
            "video_id": self.video_id,
            "video_img": Get_network_address(self.video_img_adr, self.video_img_fid),
            "video_name": self.video_name,
            "video_like": self.video_like,
            "video_view": self.video_view,
        }


class User(db.Model):
    # 用户ID，唯一主键
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 姓名
    user_name = db.Column(db.String(64), unique=True)
    # 等级/类型
    user_level = db.Column(db.Integer, db.ForeignKey('level.level_id'))
    # 过期时间
    user_expired = db.Column(db.DateTime)
    # 支付宝号
    user_ali = db.Column(db.String(24))
    # 微信号
    user_wx = db.Column(db.String(24))
    # 银行卡号
    user_bank = db.Column(db.String(24))
    # 创建与video表的关联
    videos = db.relationship('Video', backref='user', secondary=like)
    # 创建与level表的关联
    level = db.relationship('Level', backref='user')


class Tag(db.Model):
    # 标签名，唯一主键
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名字
    tag_name = db.Column(db.String(12))
    # 喜欢
    tag_like = db.Column(db.Integer, default=0)
    # 封面
    tag_img = db.Column(db.Integer)
    # 创建video的关联
    videos = db.relationship('Video', backref='tag', secondary=video_tag)


class Ad(db.Model):
    # 广告ID，唯一主键
    ad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 广告图
    ad_img = db.Column(db.String(128))
    # 广告链接
    ad_link = db.Column(db.String(128))
    # 激活状态
    ad_active = db.Column(db.Boolean, default=False)
    # 位置
    ad_seat = db.Column(db.Integer)


class Order(db.Model):
    # 订单ID，唯一主键
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键用户ID
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # 外键等级
    level = db.Column(db.Integer, db.ForeignKey('level.level_id'))
    # 流水号
    order_index = db.Column(db.String(64))
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    # 支付时间
    pay_time = db.Column(db.DateTime)
    # 数量
    order_number = db.Column(db.Integer)
    # 用户名,与user表关联
    username = db.relationship('User', backref='order')
    # level名,与level表关联
    levelname = db.relationship('Level')

    def order_info(self):
        create_time = self.create_time
        if create_time:
            create_time = datetime.datetime.strftime(create_time, "%Y-%m-%-d %H:%M:%S")

        pay_time = self.pay_time
        if pay_time:
            pay_time = datetime.datetime.strftime(pay_time, "%Y-%m-%-d %H:%M:%S")

        return {
            "order_index": self.order_index,
            "create_time": create_time,
            "pay_time": pay_time,
            "order_number": self.order_number,
            "user": self.username.user_name,
            "level": self.levelname.level_name
        }


class Level(db.Model):
    # 等级ID，唯一主键
    level_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 等级名称
    level_name = db.Column(db.String(12))
    # 价格
    level_price = db.Column(db.Integer)
    # 有效时间
    level_time = db.Column(db.Integer)
    # 激活
    level_active = db.Column(db.Boolean, default=False)

    def level_info(self):
        return {
            "level_id": self.level_id,
            "level_name": self.level_name,
            "level_price": self.level_price,
            "level_time": self.level_time,
            "level_active": self.level_active
        }


class Actor(db.Model):
    # 演员ID，唯一主键
    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 演员名字
    actor_name = db.Column(db.String(24))
    # 喜欢
    actor_like = db.Column(db.Integer, default=0)
    # 封面图片地址
    actor_img = db.Column(db.String(24))
    # 简介
    actor_desc = db.Column(db.String(128))
    # 地址
    actor_addr = db.Column(db.String(24))
    # 密匙
    actor_fid = db.Column(db.String(24))

    def actor_info(self):
        return {
           "actor_id" : self.actor_id,
           "actor_name": self.actor_name,
           "actor_like": self.actor_like,
           "actor_img": Get_network_address(self.actor_addr, self.actor_fid),
        }
    
    def actor_simple_info(self):
        return {
           "actor_id" : self.actor_id,
           "actor_name": self.actor_name,
        }