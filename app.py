from flask import Flask
from blueprint.blueprint import app as blueprint_app
from flask_sqlalchemy import SQLAlchemy
import config
import utils

app = Flask(__name__)
app.register_blueprint(blueprint_app)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.APP_SECRET_KEY
utils.db.init_app(app)

with app.app_context():
    utils.db.create_all()





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
