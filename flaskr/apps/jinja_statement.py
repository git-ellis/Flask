from flask import Flask, render_template
import os

# 初始化Flash物件
app = Flask(__name__)


@app.route('/login_page')
def show_login_page():
    return render_template("login.html")


@app.route('/registration')
def show_registration_page():
    return render_template("registration.html")


if __name__ == '__main__':
    app.run(debug=True)
