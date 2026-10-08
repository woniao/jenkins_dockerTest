from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Jenkins + Docker! 阶段2闭环跑通了'
