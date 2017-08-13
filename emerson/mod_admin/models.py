from emerson import db
from datetime import datetime


class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("newsarticles", lazy=True))

    def __init__(self, id, title, content, user_id, user):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.user = user

    def __repr__(self):
        return '<NewsArticle %r>' % self.title


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    location = db.Column(db.String(256), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    link = db.Column(db.String(256))
    remarks = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("events", lazy=True))

    def __init__(self, id, name, location, date, link, remarks, user_id, user):
        self.id = id
        self.name = name
        self.location = location
        self.date = date
        self.link = link
        self.remarks = remarks
        self.user_id = user_id
        self.user = user

    def __repr__(self):
        return '<Event %r>' % self.name


class AppText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(256), unique=True, nullable=False)
    site = db.Column(db.String(256), nullable=False)
    text = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("apptexts", lazy=True))

    def __init__(self, id, keyword, text, site, user_id, user):
        self.id = id
        self.keyword = keyword
        self.text = text
        self.site = site
        self.user_id = user_id
        self.user = user

    def __repr__(self):
        return '<AppText %r>' % self.keyword


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    embeded_link = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("videos", lazy=True))

    def __init__(self, id, embeded_link, user_id, user):
        self.id = id
        self.embeded_link = embeded_link
        self.user_id = user_id
        self.user = user

    def __repr__(self):
        return '<Video %r>' % self.embeded_link