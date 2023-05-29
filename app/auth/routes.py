from app.auth import auth

from flask import render_template,redirect,url_for
from flask_login import login_user,LoginManager,login_required

from app.auth.forms import LoginForm,RegisterForm

from app.models.auth import User
from app.extensions import bcrypt,db,login_manager

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(first_name=form.first_name.data,last_name=form.last_name.data,
                        phone_number=form.phone_number.data,
                        email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


# used for login user using their ids
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    return redirect(url_for('auth.login'))

