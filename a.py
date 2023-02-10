from flask import Flask, url_for, request, render_template

app = Flask(__name__)



@app.route('/index/<t>')
def index(t):
    return render_template('a.html', ttttttt=t)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
