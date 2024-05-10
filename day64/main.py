from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get("API_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


class MovieForm(FlaskForm):
    rating = StringField("Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired(), Length(max=35)])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    button = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieForm()
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = request.form.get("rating")  # or form.rating.data
        movie_to_update.review = request.form.get("review")  # or form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_update, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/find", methods=["GET", "POST"])
def find():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_pick = request.form.get("title")
        params = {
            "query": movie_to_pick,
            "api_key": API_KEY,
        }
        response = requests.get('https://api.themoviedb.org/3/search/movie?', params=params)
        data = response.json()["results"]
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/add")
def add():
    movie_id = request.args.get("id")
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}")
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"][0:4],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
