import logbook
from app import pity
from .decorator import SingletonDecorator   # 从decorator.py中导入装饰器类

@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self, name='pity', filename=pity.config['LOG_NAME']):
        """
        :param name: 业务名称
        :param filename: 文件名
        
        """
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        logbook.set_datetime_format("local")
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)
    
    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)
    
    def waring(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)
    
    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)