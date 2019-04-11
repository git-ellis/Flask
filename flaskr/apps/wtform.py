from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.config["SECRET_KEY"] = 'This key is very hard to guess, I think:)'


class RegistrationForm(Form):
    username = StringField(label="用戶名", validators=[validators.DataRequired(message="請輸入用戶名")])
    password = PasswordField("密碼", [validators.DataRequired("請輸入密碼"), validators.EqualTo('password')])
    double_checked_pwd = PasswordField("請確認密碼", [validators.DataRequired("請輸入密碼")])
    email = StringField("Email", [validators.DataRequired("請輸入Email"), validators.Email("無效的Email")])


@app.route("/")
def first_page():
    return render_template("registration_for_wtform.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate():
            return render_template("result.html", result="註冊成功")
        else:
            return render_template("registration_for_wtform.html", form=form)

    return render_template("registration_for_wtform.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
