from app import pity
from app.untils.logger import Log
from app import dao
from app.controller.auth.user import auth
from datetime import datetime

# 注册蓝图
pity.register_blueprint(auth)

@pity.route('/')
def hello_world():
    log = Log(" hello world专用")
    log.info("有人访问你的网站了")
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    print(now)
    return now


if __name__ == '__main__':
    pity.run("0.0.0.0",threaded=True,port="7777")


