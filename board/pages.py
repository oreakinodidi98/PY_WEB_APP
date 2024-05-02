# import blueprints, this are modules that contain related views that you can conveniently import in __init__.py
from flask import Blueprint , render_template, request

#create instance of blueprint, pages is the name of the blueprint, __name__ is the name of the module
bp = Blueprint('pages', __name__)

# define home view page
@bp.route('/')
def home():
    return render_template('pages/home.html')

# define about view page
@bp.route('/about')
def about():
    return render_template('pages/about.html')

# define contact view page
@bp.route('/contact')
def contact():
    return render_template('pages/contact.html')
