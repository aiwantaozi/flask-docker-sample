from flask import Flask, request
import json


app = Flask(__name__)
text = ""


def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    # 接收到的请求体是字节流，需要解码decode为utf-8，再转换成jason格式
    payload = req.decode("utf-8").replace('\'', '\"')
    payload = json.loads(payload)
    return payload


@app.route('/', methods=['GET'])
def index():
    # 单纯用与测试服务器是否正常运行，默认端口为5000，执行时可以修改端口
    """
    Go to localhost:5000 to see a message
    """
    return f'This is a website fot testing', 200, None


@app.route("/myhook", methods=['POST'])
# 用来接收推送，往这个url发送信息。
def mybot():
    global text
    # request.get_date()获取请求体的数据
    text = parse_request(request.get_data())
    # 正常情况下以下代码为处理接收到的数据
    print(text)
    return 'Send OK', 200


@app.route("/hook/text", methods=['GET'])
# 仅测试用展示信息，非必要
def get_notification():
    return text


if __name__ == "__main__":
    # host=‘0.0.0.0’可以被本地主机外的主机访问，port指定端口
    app.run(host='0.0.0.0', port=8080)
