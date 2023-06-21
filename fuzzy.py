import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from analise import analise


RATINGS_FILE: str = "movies_dataset/ratings_small_small.csv"
MOVIES_FILE: str = "movies_dataset/movies_metadata.csv"
LINKS_FILE: str = "movies_dataset/links_small.csv"

DICIONARIO = {}

def hated(rating: float) -> float:

    if rating > 2.0:
        return 0.0
    elif rating <= 2.0:
        return 1.0
    else:
        return 0.0


def regular(rating: float) -> float:

    if rating <= 2.0:
        return 0.0
    elif rating > 2.0 and rating < 4.0:
        return 1.0
    else:
        return 0.0


def loved(rating: float) -> float:

    if rating < 4.0:
        return 0.0
    elif rating >= 4.0:
        return 1.0
    else:
        return 0.0


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
    

def classificacao(ratings) -> str:
    if ratings[0] == 100.0:
        return 'ACLAMADO'
    elif ratings[1] == 100.0:
        return 'REGULAR'
    elif ratings[2] == 100.0:
        return 'ODIADO'

def return_(row):

    with open(LINKS_FILE, 'r', newline='', encoding='utf-8') as arq:
        links = csv.DictReader(arq)
        imdb_id = "tt"+findImdbId(row["movieId"], links)
        with open(MOVIES_FILE, 'r', newline='', encoding='utf-8') as arquivo:
            movies = csv.DictReader(arquivo)
            rating = row["rating"]

            return float(rating), findName(imdb_id, movies)


def print_ratings(row):

    rating, name = return_(row)
    loved_rating = loved(float(rating)) * 100
    regular_rating = regular(float(rating)) * 100
    hated_rating = hated(float(rating)) * 100
    
    resultado = classificacao([loved_rating, regular_rating, hated_rating])

    print(
        f" | RATING: {rating}"
        + f" | RESULTADO: {resultado} |"
        + f" | NAME: {name} |"
    )

    DICIONARIO[name] = [float(rating), [float(loved_rating), float(regular_rating), float(hated_rating)], resultado]


def main():
    with open(RATINGS_FILE, 'r', newline="", encoding='utf-8') as ratings_file:
        ratings = csv.DictReader(ratings_file)

        for row in ratings:
            print_ratings(row)

        json_string = json.dumps(DICIONARIO, indent = 2, ensure_ascii = False)

        with open("movies.json", "w+", encoding='utf-8') as outfile:
            outfile.write(json_string)

if __name__ == "__main__":
    main()