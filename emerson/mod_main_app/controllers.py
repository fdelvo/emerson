from flask import Blueprint, render_template

mod_main_app = Blueprint('main', __name__, url_prefix='/', template_folder='/templates/main/')


@mod_main_app.route('')
@mod_main_app.route('index')
def index():
    return render_template('main/index.html')


@mod_main_app.route('about')
def about():
    return render_template('main/about.html')


@mod_main_app.route('news')
def news():
    return render_template('main/news.html')


@mod_main_app.route('music')
def music():
    return render_template('main/music.html')


@mod_main_app.route('events')
def events():
    return render_template('main/events.html')


@mod_main_app.route('contact')
def contact():
    return render_template('main/contact.html')
