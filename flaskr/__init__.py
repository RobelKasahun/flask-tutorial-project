'''
    - __init__.py
        - contains the application factory, and it tells Python that 
          the flaskr directory should be treated as a package.
'''
import os
from flask import Flask

# create_app is the application factory function.
def create_app(test_config=None):
    '''
        Create and configure the app
    '''
    # Create an instance of Flask
    # __name__ represents the current file [ __init__.py ] or module
    '''
        The app needs to know where it’s located to set up 
        some paths, and __name__ is a convenient way to tell it that.
    '''
    # instance_relative_config=True tells the app that 
    # configuration files are relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_mapping() sets some default configuration that the app will use:
    app.config.from_mapping(
        # SECRET_KEY is used by Flask and extensions to keep data safe.
        SECRET_KEY='dev',
        # DATABASE is the path where the SQLite database file will be saved. It’s under 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        '''
            overrides the default configuration with values taken from the config.py 
            file in the instance folder if it exists. For example, when deploying, 
            this can be used to set a real SECRET_KEY.
        '''
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    try:
        # ensure the instance folder exists
        # create a directory named instance
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # a simple page that says hello
    @app.route('/')
    def index():
        return f'Hello, World!!!'
    
    return app