# flask 构造一个简易的接口web服务
# flask核心比django轻量,依赖各种插件,蓝图实现类似django架构
# 安装pip install flask  安装完成后会发现一些依赖包,flask核心代码.jinjia2前端模板渲染.werzurg封装了http请求响应

from flask import Flask
import json

app = Flask(__name__)

from flask_cors import CORS     # 解决跨域问题
CORS(app,supports_credentials = True)


@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():
    resp = {
        "msg":'26126216'
    }
    resp =json.dumps(resp)

    return resp
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)