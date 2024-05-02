from flask import Blueprint , render_template, request, current_app

def page_not_found(e):
    current_app.logger.info(f"'{e.name}' error ({e.code}) at {request.url}")
    return render_template('errors/404.html'), 404