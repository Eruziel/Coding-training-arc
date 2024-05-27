def movie_organizer(*args):
    movies = {}

    for name, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(name)

    sorted_movies = sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''

    for genre, names in sorted_movies:
        result += f"{genre} - {len(names)}\n"
        for value in sorted(names):
            result += ''.join(f"* {value}\n")

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))


