from flask import Flask, render_template, request
# connect pages blueprint to the app
import pages
import posts
import database
import os
import errors
from dotenv import load_dotenv
from database import init_db_command

# load environment variables
load_dotenv()

# application factory
def create_app():
    # makes app a flask application
    app = Flask(__name__)
    # gives you acces to load enviroment variables from the .env file that start with FLASK_ , then it will strip the FLASK_ prefix and set the rest of the key as a config variable
    app.config.from_prefixed_env()
    # display log level of info and above
    app.logger.setLevel('INFO')
    # initialize the app with the config file from database.py
    database.init_app(app)
    # initialize the app with the config file from pages.py
    app.register_blueprint(pages.bp)
    # initialize the app with the config file from posts.py
    app.register_blueprint(posts.bp)
    # initialize the app with the config file from errors.py
    app.register_error_handler(404, errors.page_not_found)
    # print out current enviroment variable
    app.logger.debug(f'\nCurrent Enviroment:{os.getenv("ENVIRONMENT")}')
    # print out database name
    app.logger.debug(f'\nUsing Database:{app.config.get("DATABASE")}')
    #initializes the app and returns it. 
    return app

# run the app
app = create_app()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    with app.app_context():
        init_db_command()
    