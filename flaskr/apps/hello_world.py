from flask import Flask
import os

# 初始化Flash物件
app = Flask(__name__)

'''
app.route(rule, options)
rule: URL
options: 可選參數
'''


@app.route('/')
def hollow_world():
    print(os.path.join(app.instance_path, 'flaskr.sqlite'))
    return '<h1>Hello world!</h1>'


if __name__ == '__main__':
    '''
        app.run(host, port, debug, options)
        run():執行應用程式在伺服器上
        host:伺服器主機名稱，默認127.0.0.1(localhost)，如果設置0.0.0.0則可以由外部ip訪問
        port: 默認5000
        debug: 預設False，每次修改程式需要自己重開server，設置Ture之後則會自動重新佈署
        options:可選參數
    '''
    app.run(host='0.0.0.0', debug=True)
