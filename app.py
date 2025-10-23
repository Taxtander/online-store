from flask import Flask
from blueprint.blueprint import app as blueprint_app

app = Flask(__name__)
app.register_blueprint(blueprint_app)



if __name__ == "__main__":
    app.run()
