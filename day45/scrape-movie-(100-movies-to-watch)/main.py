import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
