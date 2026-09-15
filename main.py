movies = [
    {"title": "Интерстеллар", "genre": "Фантастика", "rating": 8.7, "tickets": 12},
    {"title": "Начало", "genre": "Фантастика", "rating": 8.8, "tickets": 0},
    {"title": "Джокер", "genre": "Драма", "rating": 8.4, "tickets": 7},
    {"title": "Гладиатор", "genre": "История", "rating": 8.5, "tickets": 3},
]


def show_movies(movies: list[dict[str | int, str]]) -> None:
    for movie in movies:
        print(
            f"{movie['title']} | "
            f"{movie['genre']} | "
            f"рейтинг: {movie['rating']} | "
            f"билетов: {movie['tickets']}"
        )


show_movies(movies)