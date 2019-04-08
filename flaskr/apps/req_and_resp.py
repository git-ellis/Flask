from flask import Flask, render_template, request, make_response
import json

app = Flask(__name__)


@app.route("/")
def first_page():
    return render_template("login.html")


@app.route("/registration")
def show_registration_page():
    return render_template("registration.html")


@app.route("/register", methods=['POST'])
def register():
    print(f"method : {request.method}")
    print(f"form : {request.form}")  # 取得form表單的參數
    print(f"args : {request.args}")  # 取的query string的參數
    print(f"values : {request.values}")  # 取得所有的參數(request object and query string)
    print(f"path : {request.path}")  # /register
    print(f"full_path : {request.full_path}")  # /register?v=1.0

    print(f"url_charset : {request.url_charset}")  # utf-8
    print(f"url_root : {request.url_root}")  # http://127.0.0.1:5000/

    print(f"url : {request.url}")  # http://127.0.0.1:5000/register?v=1.0
    print(f"base_url : {request.base_url}")  # http://127.0.0.1:5000/register
    print(f"host_url : {request.host_url}")  # http://127.0.0.1:5000/

    print(f"authorization : {request.authorization}")  # None
    print(f"blueprint : {request.blueprint}")  # None
    print(f"cache_control : {request.cache_control}")
    print(f"content_type : {request.content_type}")  # application/x-www-form-urlencoded
    print(f"cookies : {request.cookies}")  # {}
    print(f"data : {request.data}")  # b'' 應該是二進制
    print(f"date : {request.date}")  # None
    print(f"endpoint : {request.endpoint}")  # register
    print(f"files : {request.files}")

    print(f"headers : {request.headers}")
    '''
        Host: 127.0.0.1:5000
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
        Accept-Encoding: gzip, deflate
        Referer: http://127.0.0.1:5000/registration
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 55
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
    '''

    print(f"host : {request.host}")  # 127.0.0.1:5000
    print(f"json : {request.json}")  # None
    print(f"mimetype : {request.mimetype}")  # application/x-www-form-urlencoded
    print(f"mimetype_params : {request.mimetype_params}")  # {}
    print(f"query_string : {request.query_string}")  # b'v=1.0'
    print(f"user_agent : {request.user_agent}")
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0

    # request.form.get('myid') # for input
    # request.form.getlist('mychecks') # for checkbox
    # print(f"get_data : {request.get_data}")
    # print(f"get_json : {request.get_json}")

    # python 3.5 PEP448 合併dict
    result = {**request.form, **request.args}

    resp = make_response(render_template('result.html', result=result), 200)
    resp.headers['Content-Type'] = 'text/html'
    return resp


@app.route("/login", methods=['GET', 'POST'])
def login():
    # help(request.values.get)
    # print(dir(request.values))

    print(request.form)
    print(request.args)
    print(request.values)

    username = request.form.get("username", "")
    password = request.form.get("password", "")
    email = request.form.get("email", "")
    result = {"username": username, "password": password, "email": email}

    resp = make_response(render_template("result.html", result=result))
    return resp


@app.route("/postman/login", methods=['GET', 'POST'])
def postman_login():
    help(json.dumps)
    print(request.form)
    print(request.args)
    print(request.values.copy())
    print(help(request.values))
    result = {"method": request.method,
              "form": request.form.copy(),
              "args": request.args.copy(),
              "values": request.values.to_dict()}

    json_str = json.dumps(result)
    return json_str


if __name__ == '__main__':
    app.run(debug=True)
