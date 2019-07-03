from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.confs.config import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
