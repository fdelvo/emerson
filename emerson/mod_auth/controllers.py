# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for
# Import password / encryption helper tools
from flask_login import login_user, LoginManager, logout_user
from flask_user import login_required
from werkzeug.security import generate_password_hash

# Import the database object from the main app module
from emerson import db, app
# Import module models (i.e. User)
from emerson.mod_auth.models import AdminUser
from .forms import SigninForm, SignupForm

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth/', template_folder='/templates/auth/')
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return AdminUser.query.filter_by(id=user_id).first()


@mod_auth.route("logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signup'))


# Set the route and accepted methods
@mod_auth.route('signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('auth/signup.html', form=form)
        else:
            new_user = AdminUser(form.username.data, form.email.data, generate_password_hash(form.password.data), True)
            db.session.add(new_user)
            db.session.commit()

            session['email'] = new_user.email

            return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"

    elif request.method == 'GET':
        return render_template('auth/signup.html', form=form)


@mod_auth.route('login', methods=['GET', 'POST'])
def login():
    form = SigninForm()
    if request.method == 'POST':
        if form.validate():
            user = AdminUser.query.filter_by(email=form.email.data).first()
            login_user(user)
            flash('logged in')
            return render_template('auth/signin.html', form=form)
        return render_template('auth/signin.html', form=form)

    return render_template('auth/signin.html', form=form)
