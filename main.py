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


def search_to_title(string: str) -> list[dict[str, str | int]]:
    result = []
    for movie in movies:
        if string.lower().strip() in movie['title'].lower():
            result.append(movie)

    return sorted(result, key=lambda x: x['rating'])


show_movies(movies)

print('Добро пожаловать в кинотеатр!')

found = search_to_title(' интер')
show_movies(found)