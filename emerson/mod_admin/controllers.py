from flask import Blueprint, render_template

mod_admin = Blueprint('administration', __name__, url_prefix='/admin/', template_folder='/templates/admin/')


@mod_admin.route('')
@mod_admin.route('index')
def index():
    return render_template('admin/index.html')


@mod_admin.route('app_texts')
def app_texts():
    return render_template('admin/app_texts.html')


@mod_admin.route('events')
def events():
    return render_template('admin/events.html')


@mod_admin.route('news')
def news():
    return render_template('admin/news.html')


@mod_admin.route('videos')
def videos():
    return render_template('admin/videos.html')


@mod_admin.route('/admin/spotify')
def spotify():
    return render_template('admin/spotify.html')
