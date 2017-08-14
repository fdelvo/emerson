from emerson import db
from emerson.mod_admin.forms import AppTextForm, EventForm
from emerson.mod_admin.models import AppText, Event
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


@mod_admin.route('edit_app_text/<id>', methods=['GET', 'POST'])
@login_required
def edit_app_text(id):
    app_text = AppText.query.filter_by(id=id).first()
    form = AppTextForm(obj=app_text)
    form.populate_obj(app_text)
    if request.method == 'POST' and form.validate():
        app_text.text = form.text.data
        db.session.commit()
        flash("Text saved.", "success")
        return redirect(url_for('administration.app_texts'))

    return render_template('admin/edit_app_text.html', form=form, app_text=app_text)


@mod_admin.route('app_texts')
@login_required
def app_texts():
    app_texts = AppText.query.all()
    return render_template('admin/app_texts.html', app_texts=app_texts)


@mod_admin.route('events')
@login_required
def events():
    events = Event.query.all()
    return render_template('admin/events.html', events=events)


@mod_admin.route('new_event', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if request.method == 'POST':
        if form.validate():
            new_event = Event(form.name.data, form.date.data, form.location.data, form.link.data, form.remarks.data)
            db.session.add(new_event)
            db.session.commit()
            flash(f'Event "{new_event.name}" created.')
            return redirect(url_for('administration.events'))
        flash_errors(form)
        return render_template('admin/new_event.html', form=form)
    return render_template('admin/new_event.html', form=form)


@mod_admin.route('edit_event/<id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    event = Event.query.filter_by(id=id).first()
    form = EventForm(obj=event)
    form.populate_obj(event)
    if request.method == 'POST' and form.validate():
        event.name = form.name.data
        event.date = form.date.data
        event.location = form.location.data
        event.link = form.link.data
        event.remarks = event.remarks.data
        db.session.commit()
        flash(f'Event "{event.name}" saved.', 'success')
        return redirect(url_for('administration.events'))

    return render_template('admin/edit_event.html', form=form, event=event)


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


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error), "fail")
