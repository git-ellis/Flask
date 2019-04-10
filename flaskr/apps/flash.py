from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = '7545b490a4abdd17516eac423a18bcf6'  # 不要配置在程式中


# flash函數是將message存放在session中，所以需要secret_key

@app.route("/")
def show_login_page():
    return render_template("login.html")


@app.route("/success")
def show_login_succ_msg():
    return "Congratulations, login success."


"""
     flash(message, category='message')
     category 消息類別 : message, info, error, warning
"""


@app.route("/login", methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # flash可以塞很多訊息
    if len(username.strip()) != 0 and len(password.strip()):
        flash("登入成功!")
        flash("login success!")
    else:
        flash("登入失敗!", category='error')
        flash("login failed!", category='error')
    return render_template("/login.html")


if __name__ == "__main__":
    app.run(debug=True)
