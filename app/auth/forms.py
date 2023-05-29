from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField

from wtforms.validators import InputRequired,Length,ValidationError

from app.models.auth import User

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4,max=20)],
                           render_kw={"placeholer":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8,max=20)],
                           render_kw={"placeholer":"Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username=User.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError('The username already exists.Kindly choose a diffrent one')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4,max=20)],
                           render_kw={"placeholer":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8,max=20)],
                           render_kw={"placeholer":"Password"})
    submit = SubmitField("Login")