from flask import Flask, render_template
import os

# 初始化Flash物件
app = Flask(__name__)


@app.route('/phone/<int:price>')
def comment_price(price):
    return render_template("phone.html", price=price)


@app.route('/foreach/list')
def show_list():
    ls = []
    for i in range(1, 10):
        ls.append('id' + str(i))
    return render_template("show_list.html", list=ls)


@app.route('/foreach/dict')
def show_dict():
    dict = {'name': 'Jack', 'age': 50, 'height': 180, 'weight': 80}
    return render_template("show_dict.html", dict=dict)


if __name__ == '__main__':
    app.run(debug=True)
