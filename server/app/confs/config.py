
DATABASE_ADDR = "space.heyu.work"
DATABASE_PORT = "8010"
DATABASE_TYPE = "mysql+pymysql"
DATABASE_USER = "admin"
DATABASE_PSWD = "123456"
DATABASE_NAME = "test"
DATABASE_URl = DATABASE_TYPE + "://" + DATABASE_USER + ":" + DATABASE_PSWD + "@" + DATABASE_ADDR + ":" + DATABASE_PORT + "/" + DATABASE_NAME

FLIE_MASTER_ADDR = "space.heyu.work"
FLIE_MASTER_POER = "8000"
FLIE_MASTER_URL = FLIE_MASTER_ADDR + ":" + FLIE_MASTER_POER

FLIE_SROTAGE_URL = {
    "8001":{
        "URL": "space.heyu.work"
    },
    "8002":{
        "URL": "space.heyu.work"
    },
    "8003":{
        "URL": "space.heyu.work"
    }
}

class Config(object):
    DEBUG = True
    SECRET_KEY = "Flask"
    SQLALCHEMY_DATABASE_URI = DATABASE_URl
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLIE_MASTER_URL = FLIE_MASTER_URL
    FLIE_SROTAGE_URL = FLIE_SROTAGE_URL