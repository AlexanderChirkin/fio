from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        print(request.args)
        # userrole = request['userrole']
        # username = request['username']
    return render_template('main.html', title='Very main page')




if __name__ == '__main__':
    app.run()
