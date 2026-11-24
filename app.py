from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Jenkins + Docker! 阶段2闭环跑通了'
if __name__ == '__&#8203;main__':
    app.run(host='0.0.0.0', port=5000)
