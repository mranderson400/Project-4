from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from app import db
from app.account.forms import (
    ChangeEmailForm,
    ChangePasswordForm,
    CreatePasswordForm,
    LoginForm,
    RegistrationForm,
    RequestResetPasswordForm,
    ResetPasswordForm,
)
from app.models import User

account = Blueprint('account', __name__)
main = Blueprint('main', __name__)


## I don't know if we have an index page, but this could be the route for that ##

@main.route('/')
@main.route('/index')
def index():
    return redirect (url_for('index.html'))

@account.route('/login', methods=['GET', 'POST'])
def login():
    """Log in an existing user."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('You are now logged in. Welcome back!', 'success')
            
    return render_template('account/login.html', form=form)

@account.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user without sending a confirmation email."""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return render_template('account/index.html')
    return render_template('account/register.html', form=form)


#@account.route('/logout', methods=['GET', 'POST'])
#@login_required
#def logout():
#    logout_user()
#    flash('You have been logged out.', 'info')
#    # Redirect to the login page after logout
#    return render_template('account/index.html')
@account.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out.', 'info')
    else:
        flash('You are already logged out.', 'warning')
    # Redirect to the login page after logout or if already logged out
    return render_template('account/index.html')




    