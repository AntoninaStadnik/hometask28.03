import json

from fastapi import FastAPI
from pydantic import BaseModel

from settings import settings

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    with open(settings.data_file_path) as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return {"message": "Movie not found"}


@app.post("/movies")
def add_movie(movie: Movie) -> dict[str, str]:
    with open(settings.data_file_path) as file:
        movies = json.load(file)

    if settings.max_films is not None and len(movies) >= settings.max_films:
        return {"message": "Max films limit reached"}

    movies.append(movie.model_dump())

    with open(settings.data_file_path, "w") as file:
        json.dump(movies, file, indent=4)

    return {"message": "Movie added successfully!"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int) -> dict[str, str]:
    with open(settings.data_file_path) as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            break

    with open(settings.data_file_path, "w") as file:
        json.dump(movies, file, indent=4)

    return {"message": "Movie removed successfully!"}