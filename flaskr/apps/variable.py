from flask import Flask

# 初始化Flash物件
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<h1>Welcome</h1>'


@app.route('/hello')
def hollow_world():
    return '<h1>This is a normal mapping</h1>'


@app.route('/hello/')
def hollow_():
    return '<h1>This is a dictionary mapping</h1>'


"""
    目錄也可以當作一個mapping
"""


@app.route('/hello/<name>')
def hollow(name):
    # print(str(type))
    print(type(name))
    return f'<h1>Hello {name}!</h1>'


"""
    use a converter to specify the type of the argument.
    default: <string:variable_name>
    
    string 	(default) accepts any text without a slash
    int 	accepts positive integers
    float 	accepts positive floating point values
    path 	like string but also accepts slashes
    uuid 	accepts UUID strings
"""


@app.route('/show/<int:num>')
def show_int_number(num):
    return f'num = {num}'


@app.route('/show/<float:num>')
def show_float_number(num):
    return f'num = {num}'


# @app.route('/show/<string:name>')
# def show_name(name):
#     return f'string = {name}'


@app.route('/show/<path:path>')
def show_path(path):
    return f'path = {path}'


@app.route('/show/<uuid:uuid>')
def show_uuid(uuid):
    return f'uuid = {uuid}'


if __name__ == '__main__':
    '''
        app.run(host, port, debug, options)
        run():執行應用程式在伺服器上
        host:伺服器主機名稱，默認127.0.0.1(localhost)，如果設置0.0.0.0則可以由外部ip訪問
        port: 默認5000
        debug: 預設False，每次修改程式需要自己重開server，設置Ture之後則會自動重新佈署
        options:可選參數
    '''
    app.run(debug=True)
