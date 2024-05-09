from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)
today = dt.date.today().strftime("%Y")


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    name = "Burak Durdu"
    return render_template("index.html", num=random_number, today=today, name=name)


@app.route("/guess/<name>")
def guess(name):
    name_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age = name_response.json()["age"]
    gender = gender_response.json()["gender"]
    return render_template("guess.html", age=age, gender=gender, name=name)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
