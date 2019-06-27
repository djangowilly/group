from flask import render_template, redirect, url_for, flash
from sales import app, db
from sales.forms import RegistrationForm
from sales.models import User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        send_email(form.email.data)
        flash('Your account has been created, please check your email!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')



