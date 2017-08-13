from flask import Blueprint, render_template, request
from sqlalchemy import update

from emerson import db
from emerson.mod_admin.forms import AppTextForm
from emerson.mod_admin.models import AppText

mod_admin = Blueprint('administration', __name__, url_prefix='/admin/', template_folder='/templates/admin/')


@mod_admin.route('')
@mod_admin.route('index')
def index():
    return render_template('admin/index.html')


@mod_admin.route('app_texts/<app_text_id>', methods=['GET', 'PUT'])
def app_texts(app_text_id):
    form = AppTextForm()
    if request.method == 'PUT':
        app_text = AppText.query.filter_by(id=app_text_id)
        app_text.text = form.text.data
        db.session.commit()

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
