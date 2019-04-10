from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route("/")
def show_login_page():
    return render_template("login.html")


# @app.route("/success")
# def show_login_succ_msg():
#     return "Congratulations, login success."


@app.route("/success")
@app.route("/success/<string:secret>")
def show_login_succ_msg(secret):
    print("secret =", secret)
    if secret == "super_user":
        return "super user login success."

    return "login success."


'''
    url_for('func_name') # 注意:不是url mapping
    redirect(location, code=302, Response=None)
'''


@app.route("/login/<string:secret>", methods=['POST'])
@app.route("/login", methods=['POST'])
def login(secret):

    # 實現帶參數的for_url()
    if secret == "super_user":
        return redirect(url_for('show_login_succ_msg', secret="super_user"))

    username = request.form.get("username")
    password = request.form.get("password")

    if len(username.strip()) != 0 and len(password.strip()):
        return redirect(url_for('show_login_succ_msg'))
    else:
        return abort(401)


if __name__ == "__main__":
    app.run(debug=True)
