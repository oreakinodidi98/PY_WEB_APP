# import blueprints, this are modules that contain related views that you can conveniently import in __init__.py
from flask import Blueprint , render_template, request, redirect, url_for, flash , current_app
from database import get_db

#create instance of blueprint, pages is the name of the blueprint, __name__ is the name of the module
bp = Blueprint('posts', __name__)


# define create page
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author  = request.form["author"]
        message  = request.form["message"]

        if message and author:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)", (author , message )
            )
            db.commit()
            current_app.logger.info(f"New post by {author}")
            flash(f"Thanks for posting, {author}!", category="success")
            return redirect(url_for("posts.posts"))
        else:
            flash("You need to post a message.", category="error")
        
    return render_template("posts/create.html")

# define posts page
@bp.route('/posts')
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)
