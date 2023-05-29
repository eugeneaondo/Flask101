from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField

from wtforms.validators import InputRequired,Length,ValidationError

from app.models.auth import User

class RegisterForm(FlaskForm):

    first_name = StringField(validators=[InputRequired(), Length(max=20)],
                           label="First Name")
    last_name = StringField(validators=[InputRequired(), Length(max=20)],
                           label="Last Name")
    email = StringField(validators=[InputRequired(), Length(min=4,max=20)],
                           label="email")
    phone_number = StringField(validators=[InputRequired(), Length(min=4,max=20)],
                           label="Phone Number")
    password = PasswordField(validators=[InputRequired(), Length(min=8,max=20)],
                           label="Password")
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username=User.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError('The username already exists.Kindly choose a diffrent one')

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4,max=20)],
                           label="Email")
    password = PasswordField(validators=[InputRequired(), Length(min=8,max=20)],
                           label="Password")
    submit = SubmitField("Login")