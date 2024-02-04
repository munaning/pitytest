#基础类配置
import json
import os

class Config(object):
     #flask jsonify编码问题
    json.ensure_ascii = False
    ""
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log')

     #数据库配置
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "WOshishei123"
    DBNAME = "pity"

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}' .format (MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
