from watchlist import app
from watchlist.models import User
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('error/404.html'), 404