import os

from flask import Flask

'''
The Application Factory

It’s time to start coding! Create the flaskr directory and add the __init__.py file. 
The __init__.py serves double duty: it will contain the application factory,
and it tells Python that the flaskr directory should be treated as a package.
'''

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # sets some default configuration that the app will use
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # silent=Ture if you want silent failure for missing files.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
