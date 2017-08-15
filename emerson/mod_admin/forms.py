from flask_wtf import Form, widgets
from wtforms import StringField, SubmitField, validators
from wtforms_components import DateTimeField
from wtforms.widgets import TextArea


class AppTextForm(Form):
    text = StringField('Text', [validators.DataRequired("Please enter a text.")], widget=TextArea())
    submit = SubmitField("Save text")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class NewsArticleForm(Form):
    title = StringField('Title', [validators.DataRequired("Please enter a text.")])
    content = StringField('Content', [validators.DataRequired("Please enter a text.")], widget=TextArea())
    submit = SubmitField("Create news article")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class EventForm(Form):
    name = StringField('Name', [validators.DataRequired("Please enter a text.")])
    location = StringField('Location', [validators.DataRequired("Please enter a text.")])
    date = DateTimeField('Date', [validators.DataRequired("Please enter a date.")], format='%d.%m.%Y@%H:%M:%S')
    link = StringField('Link')
    remarks = StringField('Remarks', widget=TextArea())
    submit = SubmitField("Create event")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class VideoForm(Form):
    description = StringField('Description', [validators.DataRequired("Please enter a text.")])
    embedded_link = StringField('Embedded Link', [validators.DataRequired("Please enter a text.")])
    submit = SubmitField("Create video")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class SpotifyForm(Form):
    description = StringField('Description', [validators.DataRequired("Please enter a text.")])
    embedded_link = StringField('Embedded Link', [validators.DataRequired("Please enter a text.")])
    submit = SubmitField("Create spotify link")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
