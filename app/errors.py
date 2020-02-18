from app import db, app
from flask import render_template


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def not_found_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
