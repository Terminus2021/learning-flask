from flask import Flask
app = Flask(__name__)
@app.route("/test")
def hlw():
    return 'Hello World'
    return '这只是一个使用Flask构建的Python program. 由于与以前的服务器冲突，因此将会把它运作到其它终端。'
    return 'for example: Linux 比如Ubuntu。这些是自带py的。可恶的lamp'

if __name__ == '__main__':
     app.run()
