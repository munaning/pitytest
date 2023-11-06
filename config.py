#基础类配置
import json
import os

class Config(object):
     #flask jsonify编码问题
    json.ensure_ascii = False
    
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log')
   