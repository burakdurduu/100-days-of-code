from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

EMAIL = "admin@email.com"
PASSWORD = "12345678"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(granular_message=True, check_deliverability=True)])
    password = PasswordField(label="Password", validators=[Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "yoursecretkey"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == EMAIL and login_form.password.data == PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
