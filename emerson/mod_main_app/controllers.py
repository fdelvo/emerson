from flask import Blueprint, render_template
from jinja2 import Environment, environment
from sqlalchemy import desc

from emerson.mod_admin.models import AppText, NewsArticle, Video, Spotify, Event

mod_main_app = Blueprint('main', __name__, url_prefix='/', template_folder='/templates/main/')


@mod_main_app.route('')
@mod_main_app.route('index')
def index():
    return render_template('main/index.html')


@mod_main_app.route('about')
def about():
    app_texts = AppText.query.filter_by(site="about").all()
    return render_template('main/about.html', app_texts=app_texts)


@mod_main_app.route('news')
def news():
    news = NewsArticle.query.order_by(desc(NewsArticle.date)).limit(5)
    return render_template('main/news.html', news=news)


@mod_main_app.route('music')
def music():
    videos = Video.query.all()
    spotifys = Spotify.query.all()
    return render_template('main/music.html', videos=videos, spotifys=spotifys)


@mod_main_app.route('events')
def events():
    events = Event.query.all()
    return render_template('main/events.html', events=events)


@mod_main_app.route('contact')
def contact():
    app_texts = AppText.query.filter_by(site="contact").all()
    return render_template('main/contact.html', app_texts=app_texts)


