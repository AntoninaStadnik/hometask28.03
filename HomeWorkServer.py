# Напишіть сервер для збереження даних про фільми.
# Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними:
# ● id
# ● title
# ● director
# ● year
# Функціонал:
# 1. Отримання даних за ID фільму
# ○ шлях – movies/{movie_id}
# ○ метод – GET
# Додавання нового фільму
# ○ шлях – movies
# ○ метод – POST
# 3. Видалення фільму за ID
# ○ шлях – movies/{movie_id}
# ○ метод – DELETE
# Запустіть сервер
# Напишіть клієнта з таким фуннкціоналом для
# користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм

import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    with open("movies.json") as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return {"message": "Movie not found"}


@app.post("/movies")
def add_movie(movie: Movie) -> dict[str, str]:
    with open("movies.json") as file:
        movies = json.load(file)

    movies.append(movie.model_dump())

    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)

    return {"message": "Movie added successfully!"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int) -> dict[str, str]:
    with open("movies.json") as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            break

    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)

    return {"message": "Movie removed successfully!"}

