from flask import Blueprint


app = Blueprint("general", __name__)


@app.route("/")
def main_page():
    return 'this is main page'


@app.route("/about")
def about_page():
    return 'this is about page'


