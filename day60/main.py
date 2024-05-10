from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def recieve_data():
    username = request.form["username"]
    password = request.form["password"]
    return f"<h1>Username: {username} Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
