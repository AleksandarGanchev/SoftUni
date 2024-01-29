def movie_organizer(*args):
    organizer = {}
    for movie_name, genre in args:
        if genre not in organizer:
            organizer[genre] = []

        organizer[genre].append(movie_name)

    sorted_by_genre = dict(sorted(organizer.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ''
    for genre, movie_name in sorted_by_genre.items():
        sorted_movies = sorted(movie_name)
        output += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            output += f"* {name}\n"

    return output



