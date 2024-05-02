from flask import Flask, render_template, request
# connect pages blueprint to the app
import pages
import posts
import database
import os
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
    # initialize the app with the config file from database.py
    database.init_app(app)
    # initialize the app with the config file from pages.py
    app.register_blueprint(pages.bp)
    # initialize the app with the config file from posts.py
    app.register_blueprint(posts.bp)
    # print out current enviroment variable
    print(f'\nCurrent Enviroment:{os.getenv("ENVIRONMENT")}')
    # print out database name
    print(f'\nUsing Database:{app.config.get("DATABASE")}')
    #initializes the app and returns it. 
    return app

# run the app
app = create_app()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    with app.app_context():
        init_db_command()
    