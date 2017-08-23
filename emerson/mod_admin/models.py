from emerson import db
from datetime import datetime


class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    content = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("admin_user.id"), nullable=False)
    user = db.relationship("AdminUser", backref=db.backref("newsarticles", lazy=True))

    def __init__(self, title, content, date, user_id):
        self.title = title
        self.content = content
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return '<NewsArticle %r>' % self.title


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    location = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    link = db.Column(db.String())
    remarks = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("admin_user.id"), nullable=False)
    user = db.relationship("AdminUser", backref=db.backref("events", lazy=True))

    def __init__(self, name, location, date, link, remarks, user_id):
        self.name = name
        self.location = location
        self.date = date
        self.link = link
        self.remarks = remarks
        self.user_id = user_id
        self.test = 'Test'

    def __repr__(self):
        return '<Event %r>' % self.name


class AppText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(), unique=True, nullable=False)
    site = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("admin_user.id"), nullable=False)
    user = db.relationship("AdminUser", backref=db.backref("apptexts", lazy=True))

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
    description = db.Column(db.String(), unique=True, nullable=False)
    embedded_link = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("admin_user.id"), nullable=False)
    user = db.relationship("AdminUser", backref=db.backref("videos", lazy=True))

    def __init__(self, embedded_link, description, user_id):
        self.embedded_link = embedded_link
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return '<Video %r>' % self.embedded_link


class Spotify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), unique=True, nullable=False)
    embedded_link = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("admin_user.id"), nullable=False)
    user = db.relationship("AdminUser", backref=db.backref("spotifys", lazy=True))

    def __init__(self, embedded_link, description, user_id):
        self.description = description
        self.embedded_link = embedded_link
        self.user_id = user_id

    def __repr__(self):
        return '<Spotify %r>' % self.embedded_link