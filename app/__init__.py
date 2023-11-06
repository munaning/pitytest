from flask import Flask
from config import Config
from app.controller.auth.user import auth

pity = Flask(__name__)
pity.json.ensure_ascii = False
#这里注册
pity.register_blueprint(auth)

pity.config.from_object(Config)