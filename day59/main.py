from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

posts = requests.get("https://api.npoint.io/d1d51cbd3ae627a02c30").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL, password=PASSWORD)
            connect.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Form Post\n\n{name}\n{email}\n{phone}\n{message}\n")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post")
def add_post():
    return render_template("make-post.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
