from flask import Flask, render_template, request
# connect pages blueprint to the app
import pages

# # makes app a flask application
# app = Flask(__name__)


# #define routes in flask for the home page
# @app.route('/')
# def home():
#     # render_template is a function that returns a rendered template
#     return render_template('index.html')


# application factory
def create_app():
    # makes app a flask application
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    #initializes the app and returns it. 
    return app

# 
app = create_app()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)