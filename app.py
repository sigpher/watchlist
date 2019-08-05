from flask import Flask
from flask import url_for


app = Flask(__name__)
@app.route('/home')
@app.route('/index')
@app.route('/')
def hello():
    return 'Welcome to My Site'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {name}'


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('hello'))
    print(url_for('user_page',  name='choi'))
    print(url_for('user_page',  name='lora'))
    print(url_for('test_url_for', num=2, lastname='willy', firstname='choi'))
    return 'test page'

if __name__ == "__main__":
    app.run()
