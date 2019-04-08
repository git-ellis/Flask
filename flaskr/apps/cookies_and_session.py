from flask import Flask, make_response, request, session, render_template
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = '7545b490a4abdd17516eac423a18bcf6'  # 不要配置在程式中


@app.route("/")
def index():
    return render_template("login.html")


'''
    Cookies是存放在客戶端瀏覽器，
    如果要塞值進cookies請使用response物件的set_cookie
    如果要取出cookies的值請使用request物件的cookies屬性取出
'''


@app.route("/set_cookie/<user_id>")
def set_cookie(user_id):
    response = make_response("<h1>配置cookies</h1>")
    timeout = datetime.today() + timedelta(days=10) // 失效時間
    response.set_cookie("user_id", user_id)
    response.set_cookie
    # response.set_cookie("user_id", user_id, expires=timeout)
    return response


@app.route("/show_cookies")
def show_cookies():
    cookies = request.cookies
    print("cookies =", cookies)

    return f"<h1>cookies = {cookies}</h1>"


'''
    session物件和request物件一樣可以直接使用，
    要刪除session值使用session.pop('key', None) 
    None -> 如果找不到才不會拋出KeyError
'''


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get("username")
        return render_template("result.html")


@app.route("/logout")
def logout():
    print(session)
    print(dir(session))
    print(help(session.pop))
    session.pop("username", None)
    session.pop("user_id", None)
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
