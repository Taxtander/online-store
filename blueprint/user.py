from flask import Blueprint
import models.user


app = Blueprint("user", __name__)


@app.route("/user")
def user_page():
    return 'this is user page'
