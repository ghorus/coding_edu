from flask import Flask

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# For blueprints
def reg_bp():
    from coding_edu.main.routes import main
    app.register_blueprint(main)


reg_bp()
