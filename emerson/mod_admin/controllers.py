import datetime

from flask_login import current_user
from sqlalchemy import desc

from emerson import db
from emerson.mod_admin.forms import AppTextForm, EventForm, NewsArticleForm, VideoForm, SpotifyForm
from emerson.mod_admin.models import AppText, Event, NewsArticle, Video, Spotify
from flask import Blueprint, render_template
from flask import flash
from flask import redirect
from flask import request
from flask import url_for
from flask.ext.login import login_required

mod_admin = Blueprint('administration', __name__, url_prefix='/admin/', template_folder='/templates/admin/')
PAGE_SIZE = 50


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


@mod_admin.route('app_texts', defaults={'page': 1})
@mod_admin.route('app_texts/page/<int:page>')
@login_required
def app_texts(page):
    app_texts = AppText.query.order_by(desc(AppText.id)).paginate(page, PAGE_SIZE)
    return render_template('admin/app_texts.html', app_texts=app_texts)


@mod_admin.route('events', defaults={'page': 1})
@mod_admin.route('events/page/<int:page>')
@login_required
def events(page):
    events = Event.query.order_by(desc(Event.date)).paginate(page, PAGE_SIZE)
    return render_template('admin/events.html', events=events)


@mod_admin.route('new_event', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if request.method == 'POST' and not request.json:
        print(request.data)
        if form.validate():
            new_event = Event(form.name.data, form.location.data, form.date.data, form.link.data, form.remarks.data,
                              current_user.id)
            db.session.add(new_event)
            db.session.commit()
            flash(f'Event "{new_event.name}" created.', 'success')
            return redirect(url_for('administration.events'))
        flash_errors(form)
        return render_template('admin/new_event.html', form=form)
    if request.method == 'POST' and request.json:
        new_event = Event(request.json['name'], request.json['location'], request.json['date'], request.json['link'],
                          request.json['remarks'],
                          current_user.id)
        db.session.add(new_event)
        db.session.commit()
        flash(f'Events successfully imported from Facebook.', 'success')
        return redirect(url_for('administration.events'))
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
        event.remarks = form.remarks.data
        db.session.commit()
        flash(f'Event "{event.name}" saved.', 'success')
        return redirect(url_for('administration.events'))

    return render_template('admin/edit_event.html', form=form, event=event)


@mod_admin.route('delete_event/<id>', methods=['GET'])
@login_required
def delete_event(id):
    event = Event.query.filter_by(id=id).first()
    db.session.delete(event)
    db.session.commit()
    flash(f'Event "{event.name}" deleted.', 'success')
    return redirect(url_for('administration.events'))


@mod_admin.route('news', defaults={'page': 1})
@mod_admin.route('news/page/<int:page>')
@login_required
def news(page):
    news_articles = NewsArticle.query.order_by(desc(NewsArticle.date)).paginate(page, PAGE_SIZE)
    return render_template('admin/news.html', news_articles=news_articles)


@mod_admin.route('new_news_article', methods=['GET', 'POST'])
@login_required
def new_news_article():
    form = NewsArticleForm()
    if request.method == 'POST':
        if form.validate():
            new_news_article = NewsArticle(form.title.data, form.content.data, datetime.datetime.now(), current_user.id)
            db.session.add(new_news_article)
            db.session.commit()
            flash(f'News article "{new_news_article.title}" created.', 'success')
            return redirect(url_for('administration.news'))
        flash_errors(form)
        return render_template('admin/new_news_article.html', form=form)
    return render_template('admin/new_news_article.html', form=form)


@mod_admin.route('edit_news_article/<id>', methods=['GET', 'POST'])
@login_required
def edit_news_article(id):
    news_article = NewsArticle.query.filter_by(id=id).first()
    form = NewsArticleForm(obj=news_article)
    form.populate_obj(news_article)
    if request.method == 'POST' and form.validate():
        news_article.title = form.title.data
        news_article.content = form.content.data
        db.session.commit()
        flash(f'News Article "{news_article.title}" saved.', 'success')
        return redirect(url_for('administration.news'))

    return render_template('admin/edit_news_article.html', form=form, news_article=news_article)


@mod_admin.route('delete_news_article/<id>', methods=['GET'])
@login_required
def delete_news_article(id):
    news_article = NewsArticle.query.filter_by(id=id).first()
    db.session.delete(news_article)
    db.session.commit()
    flash(f'News article "{news_article.title}" deleted.', 'success')
    return redirect(url_for('administration.news'))


@mod_admin.route('videos', defaults={'page': 1})
@mod_admin.route('videos/page/<int:page>')
@login_required
def videos(page):
    videos = Video.query.order_by(desc(Video.id)).paginate(page, PAGE_SIZE)
    return render_template('admin/videos.html', videos=videos)


@mod_admin.route('new_video', methods=['GET', 'POST'])
@login_required
def new_video():
    form = VideoForm()
    if request.method == 'POST':
        if form.validate():
            new_video = Video(form.embedded_link.data, form.description.data, current_user.id)
            db.session.add(new_video)
            db.session.commit()
            flash(f'Video "{new_video.embedded_link}" created.')
            return redirect(url_for('administration.videos'))
        flash_errors(form)
        return render_template('admin/new_video.html', form=form)
    return render_template('admin/new_video.html', form=form)


@mod_admin.route('delete_video/<id>', methods=['GET'])
@login_required
def delete_video(id):
    video = Video.query.filter_by(id=id).first()
    db.session.delete(video)
    db.session.commit()
    flash(f'Video "{video.description}" deleted.', 'success')
    return redirect(url_for('administration.videos'))


@mod_admin.route('edit_video/<id>', methods=['GET', 'POST'])
@login_required
def edit_video(id):
    video = Video.query.filter_by(id=id).first()
    form = VideoForm(obj=video)
    form.populate_obj(video)
    if request.method == 'POST' and form.validate():
        video.description = form.description.data
        video.embedded_link = form.embedded_link.data
        db.session.commit()
        flash(f'Video "{video.embedded_link}" saved.', 'success')
        return redirect(url_for('administration.videos'))

    return render_template('admin/edit_video.html', form=form, video=video)


@mod_admin.route('spotify', defaults={'page': 1})
@mod_admin.route('spotify/page/<int:page>')
@login_required
def spotify(page):
    spotifys = Spotify.query.order_by(desc(Spotify.id)).paginate(page, PAGE_SIZE)
    return render_template('admin/spotify.html', spotifys=spotifys)


@mod_admin.route('new_spotify', methods=['GET', 'POST'])
@login_required
def new_spotify():
    form = SpotifyForm()
    if request.method == 'POST':
        if form.validate():
            new_spotify = Spotify(form.embedded_link.data, form.description.data, current_user.id)
            db.session.add(new_spotify)
            db.session.commit()
            flash(f'Spotify link "{new_spotify.embedded_link}" created.')
            return redirect(url_for('administration.spotify'))
        flash_errors(form)
        return render_template('admin/new_spotify.html', form=form)
    return render_template('admin/new_spotify.html', form=form)


@mod_admin.route('edit_spotify/<id>', methods=['GET', 'POST'])
@login_required
def edit_spotify(id):
    spotify = Spotify.query.filter_by(id=id).first()
    form = SpotifyForm(obj=spotify)
    form.populate_obj(spotify)
    if request.method == 'POST' and form.validate():
        spotify.description = form.description.data
        spotify.embedded_link = form.embedded_link.data
        db.session.commit()
        flash(f'Spotify link "{spotify.embedded_link}" saved.', 'success')
        return redirect(url_for('administration.spotify'))

    return render_template('admin/edit_spotify.html', form=form, spotify=spotify)


@mod_admin.route('delete_spotify/<id>', methods=['GET'])
@login_required
def delete_spotify(id):
    spotify = Spotify.query.filter_by(id=id).first()
    db.session.delete(spotify)
    db.session.commit()
    flash(f'Spotify link "{spotify.description}" deleted.', 'success')
    return redirect(url_for('administration.spotify'))


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error), "fail")
