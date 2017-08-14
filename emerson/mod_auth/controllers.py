# Import flask dependencies
from urllib.parse import urlparse, urljoin

from emerson import db, app
from emerson.mod_auth.models import AdminUser
from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for
from flask_login import login_user, LoginManager, logout_user, login_required
from werkzeug.security import generate_password_hash

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
    return redirect(url_for('auth.test'))


@mod_auth.route("test")
@login_required
def test():
    print("Access")
    return render_template('auth/test.html')


# Set the route and accepted methods
@mod_auth.route('signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash_errors(form)
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
            next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            if not is_safe_url(next):
                return app.abort(400)

            return redirect(next or url_for('auth.signup'))

        flash_errors(form)
        return render_template('auth/signin.html', form=form)

    return render_template('auth/signin.html', form=form)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error), "fail")
