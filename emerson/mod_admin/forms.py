from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators


class AppTextForm(Form):
    username = StringField("Username", [validators.DataRequired("Please enter your first name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        if self.email.data != "florian.delvo@googlemail.com":
            self.email.errors.append("That email address is not valid.")
            return False

        user = AdminUser.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken.")
            return False
        else:
            return True