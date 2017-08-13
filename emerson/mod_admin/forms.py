from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators, DateField


class AppTextForm(Form):
    text = StringField('Text', [validators.DataRequired("Please enter a text.")])
    submit = SubmitField("Save text")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class NewsArticleForm(Form):
    title = StringField('Title', [validators.DataRequired("Please enter a text.")])
    content = StringField('Content', [validators.DataRequired("Please enter a text.")])
    submit = SubmitField("Create news article")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class EventForm(Form):
    name = StringField('Name', [validators.DataRequired("Please enter a text.")])
    location = StringField('Location', [validators.DataRequired("Please enter a text.")])
    date = DateField('Date', [validators.DataRequired("Please enter a date.")])
    link = StringField('Link')
    remarks = StringField('Remarks')
    submit = SubmitField("Create event")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class VideoForm(Form):
    embeded_link = StringField('Embeded Link', [validators.DataRequired("Please enter a text.")])
    submit = SubmitField("Create video")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True

