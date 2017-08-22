from flask import Blueprint, render_template
from jinja2 import Environment, environment
from sqlalchemy import desc
from datetime import datetime

from emerson.mod_admin.models import AppText, NewsArticle, Video, Spotify, Event

mod_main_app = Blueprint('main', __name__, url_prefix='/', template_folder='/templates/main/')
page_size = 5


@mod_main_app.route('')
@mod_main_app.route('index')
def index():
    return render_template('main/index.html')


@mod_main_app.route('about')
def about():
    app_texts = AppText.query.filter_by(site="about").all()
    return render_template('main/about.html', app_texts=app_texts)


@mod_main_app.route('news', defaults={'page': 1})
@mod_main_app.route('news/page/<int:page>')
def news(page):
    news = NewsArticle.query.order_by(desc(NewsArticle.date)).paginate(page, page_size)
    print(news)
    return render_template('main/news.html', news=news)


@mod_main_app.route('music')
def music():
    videos = Video.query.all()
    spotifys = Spotify.query.all()
    return render_template('main/music.html', videos=videos, spotifys=spotifys)


@mod_main_app.route('events', defaults={'page': 1})
@mod_main_app.route('events/page/<int:page>')
def events(page):
    events = Event.query.order_by(desc(Event.date)).paginate(page, page_size)
    return render_template('main/events.html', events=events)


@mod_main_app.route('contact')
def contact():
    app_texts = AppText.query.filter_by(site="contact").all()
    return render_template('main/contact.html', app_texts=app_texts)
