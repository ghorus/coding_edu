from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
print(os.environ.get("DATABASE_URL"))
db = SQLAlchemy(app)


# For blueprints
def reg_bp():
    from coding_edu.main.routes import main
    app.register_blueprint(main)


reg_bp()
