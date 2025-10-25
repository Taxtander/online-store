from flask import Blueprint,render_template

from models.product import Product

app = Blueprint("general", __name__)


@app.route("/")
def main_page():
    products = Product.query.all()
    return render_template("general/main.html",products=products)

@app.route("/about")
def about_page():
    return render_template("general/about.html")


