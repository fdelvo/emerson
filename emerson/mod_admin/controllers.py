from emerson import db
from emerson.mod_admin.forms import AppTextForm
from emerson.mod_admin.models import AppText
from flask import Blueprint, render_template
from flask import flash
from flask import redirect
from flask import request
from flask import url_for
from flask.ext.login import login_required

mod_admin = Blueprint('administration', __name__, url_prefix='/admin/', template_folder='/templates/admin/')


@mod_admin.route('')
@mod_admin.route('index')
@login_required
def index():
    return render_template('admin/index.html')


@mod_admin.route('app_text_edit/<id>', methods=['GET', 'POST'])
@login_required
def app_text_edit(id):
    app_text = AppText.query.filter_by(id=id).first()
    form = AppTextForm(obj=app_text)
    form.populate_obj(app_text)
    if request.method == 'POST':
        app_text.text = form.text.data
        db.session.commit()
        flash("Text saved.", "success")
        return redirect(url_for('administration.app_texts'))

    return render_template('admin/app_text_edit.html', form=form, app_text=app_text)


@mod_admin.route('app_texts')
@login_required
def app_texts():
    app_texts = AppText.query.all()
    return render_template('admin/app_texts.html', app_texts=app_texts)


@mod_admin.route('events')
@login_required
def events():
    return render_template('admin/events.html')


@mod_admin.route('news')
@login_required
def news():
    return render_template('admin/news.html')


@mod_admin.route('videos')
@login_required
def videos():
    return render_template('admin/videos.html')


@mod_admin.route('/admin/spotify')
@login_required
def spotify():
    return render_template('admin/spotify.html')
