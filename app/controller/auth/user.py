from flask import Blueprint
from flask import jsonify
from flask import request
from app.dao.auth import UserDao


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():
    # return jsonify(dict(status=200, msg="注册成功"))
    #获取request请求数据
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(status=101, msg="用户名或密码不能为空"))
    email, name = data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(status=101, msg="邮箱或姓名不能为空"))
    err = UserDao.register_user(username, name, password, email) 
    if err is not None:
        return jsonify(dict(status=101, msg=err))   
    return jsonify(dict(status=0, msg="注册成功"))
