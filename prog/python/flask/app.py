from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"


if __name__ == "__main__":
    app.debug = False
    # 在这设置IP及端口号是无效的
    app.run(host='0.0.0.0', port=8000)
