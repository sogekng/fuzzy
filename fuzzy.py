import csv
import json

RATINGS_FILE: str = "movies_dataset/ratings_small_small.csv"
MOVIES_FILE: str = "movies_dataset/movies_metadata.csv"
LINKS_FILE: str = "movies_dataset/links_small.csv"

DICIONARIO = {}


def hated(rating: float) -> float:
    # 1.5- < 100%
    # 1.5 <-> 3.0 x%
    # 3.0+ = 0%

    if rating >= 3.0:
        return 0.0
    elif rating <= 1.5:
        return 1.0
    else:
        return (rating - 1.5) / 1.5


def regular(rating: float) -> float:
    # 2.5 <-> 3.5 100%
    # 1.5 <-> 2.5 x%
    # 3.5 <-> 4.5 +x%
    # 4.5+ 100%

    if rating <= 1.5:
        return 0.0
    elif rating > 1.5 and rating < 2.5:
        return (rating - 1.5) / 1.5
    elif rating >= 2.5 and rating <= 3.5:
        return 1.0
    elif rating > 3.5 and rating < 4.5:
        return (rating - 3.5) / 1.5
    else:
        return 0.0


def loved(rating: float) -> float:
    # 4.0+ 100%
    # 2.0 <-> 4.0 x%
    # 2.0 0%

    if rating <= 2.0:
        return 0.0
    elif rating >= 4.0:
        return 1.0
    else:
        return (rating - 2.0) / 2.0


def findName(imdb_id, data):
    movie = next(filter(lambda row: row["imdb_id"] == imdb_id, data), None)

    if movie == None:
        return 'ImdbId não encontrado'
    else:
        return movie["original_title"]
    
    
def findImdbId(movieId, data):
    movieId = next(filter(lambda row: row["movieId"] == movieId, data), None)

    if movieId == None:
        return 'MovieId não encontrado'
    else:
        return movieId['imdbId']


def return_(row):

    with open(LINKS_FILE, 'r', newline='') as arq:
        links = csv.DictReader(arq)
        imdb_id = "tt"+findImdbId(row["movieId"], links)
        with open(MOVIES_FILE, 'r', newline='') as arquivo:
            movies = csv.DictReader(arquivo)
            rating = row["rating"]

            return float(rating), findName(imdb_id, movies)


def print_ratings(row):

    rating, name = return_(row)
    loved_rating = loved(rating) * 100.0
    regular_rating = regular(rating) * 100.0
    hated_rating = hated(rating) * 100.0

    print(
        f" | RATING: {rating}"
        + f" | LOVED: {loved_rating}%"
        + f" | REGULAR: {regular_rating}%"
        + f" | HATED: {hated_rating}%"
        + f" | NAME: {name} |"
    )

    DICIONARIO[name] = ['{:.1f}'.format(rating), ['{:.1f}%'.format(loved_rating), '{:.1f}%'.format(regular_rating), '{:.1f}%'.format(hated_rating)]]


def main():
    with open(RATINGS_FILE, 'r', newline="") as ratings_file:
        ratings = csv.DictReader(ratings_file)

        for row in ratings:
            print_ratings(row)

        json_string = json.dumps(DICIONARIO, indent = 2, ensure_ascii = False)

        with open(f"movies.json", "w+", encoding='utf-8') as outfile:
            outfile.write(json_string)


if __name__ == "__main__":
    main()