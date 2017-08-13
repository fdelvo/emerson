from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from emerson.mod_auth.controllers import mod_auth as auth_module
from emerson.mod_main_app.controllers import mod_main_app as main_module
from emerson.mod_admin.controllers import mod_admin as admin_module

# Register blueprint(s)
app.register_blueprint(main_module)
app.register_blueprint(auth_module)
app.register_blueprint(admin_module)
