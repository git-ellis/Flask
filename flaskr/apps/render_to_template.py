from flask import Flask, render_template
import os

# 初始化Flash物件
app = Flask(__name__)


@app.route('/template/<name>')
def hollow_world(name):
    s = "Nice to meet you today, now, you are going to learn about jinja expression!"
    s1 = "  " + s + "  "
    s2 = "<p>" + s + "<p>"

    return render_template("first_template.html", name=name, messages=(s, s1, s2))


if __name__ == '__main__':
    app.run(debug=True)
