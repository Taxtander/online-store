from flask import Blueprint, render_template

app = Blueprint("admin", __name__)


@app.route("/admin/login")
def admin_page():
    return render_template("admin/login.html")
