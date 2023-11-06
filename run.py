from app import pity
from app.untils.logger import Log


@pity.route('/')
def hello_world():
    log = Log(" hello world专用")
    log.info("有人访问你的网站了")
    return 'Hello World!'


if __name__ == '__main__':
    pity.run("0.0.0.0",threaded=True,port="7777")


