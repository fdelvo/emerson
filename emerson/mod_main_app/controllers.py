from flask import Blueprint, render_template, request
from jinja2 import Environment, environment
from sqlalchemy import desc, or_
from datetime import datetime

from emerson.mod_admin.models import AppText, NewsArticle, Video, Spotify, Event

mod_main_app = Blueprint('main', __name__, url_prefix='/', template_folder='/templates/main/')
page_size = 5
page_size_events = 20


@mod_main_app.route('')
@mod_main_app.route('index')
def index():
    app_texts = AppText.query.filter_by(site="contact").all()
    return render_template('main/index.html', app_texts=app_texts)


@mod_main_app.route('about')
def about():
    app_texts = AppText.query.filter(or_(AppText.site=="about", AppText.site=="contact")).all()
    return render_template('main/about.html', app_texts=app_texts)


@mod_main_app.route('news', defaults={'page': 1})
@mod_main_app.route('news/page/<int:page>')
def news(page):
    app_texts = AppText.query.filter_by(site="contact").all()
    news = NewsArticle.query.order_by(desc(NewsArticle.date)).paginate(page, page_size)
    print(news)
    return render_template('main/news.html', news=news, app_texts=app_texts)


@mod_main_app.route('news_article/<int:id>')
def news_article(id):
    app_texts = AppText.query.filter_by(site="contact").all()
    news_article = NewsArticle.query.filter_by(id=id).first()
    return render_template('main/news_article.html', news_article=news_article, app_texts=app_texts)


@mod_main_app.route('media')
def music():
    app_texts = AppText.query.filter_by(site="contact").all()
    videos = Video.query.all()
    spotifys = Spotify.query.all()
    return render_template('main/media.html', videos=videos, spotifys=spotifys, app_texts=app_texts)


@mod_main_app.route('events', defaults={'page': 1})
@mod_main_app.route('events/page/<int:page>')
def events(page):
    app_texts = AppText.query.filter_by(site="contact").all()
    events = Event.query.filter(Event.date > datetime.now()).order_by(desc(Event.date)).paginate(page,
                                                                                                 page_size_events)
    return render_template('main/events.html', events=events, app_texts=app_texts)


@mod_main_app.route('past_events', defaults={'page': 1})
@mod_main_app.route('past_events/page/<int:page>')
def past_events(page):
    app_texts = AppText.query.filter_by(site="contact").all()
    events = Event.query.filter(Event.date < datetime.now()).order_by(desc(Event.date)).paginate(page,
                                                                                                 page_size_events)
    return render_template('main/past_events.html', events=events, app_texts=app_texts)


@mod_main_app.route('contact')
def contact():
    app_texts = AppText.query.filter_by(site="contact").all()
    return render_template('main/contact.html', app_texts=app_texts)

@mod_main_app.route('photos')
def photos():
    return render_template('main/photos.html')