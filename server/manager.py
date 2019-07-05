from app import create_app
from app.confs.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run("0.0.0.0")
    