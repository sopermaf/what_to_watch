"""
Movie suggestion handling
"""
import sys
import pandas as pd

F_DIR = 'resources/imdb_data.csv'
ARGS = sys.argv[1:]
IMDB_DATA = pd.read_csv(F_DIR)


def suggest_movie(vals, data) -> str:
    '''
    Returns a movie title as a suggestion

    Args
    ---
    None

    Returns
    ---
    str : suggestion
    '''
    name = 'space jam'

    if vals[0] == 'movie':
        data_movie = data[data.type == 'movie']
        row = data_movie.sample()
        name = row.item.tolist()[0]

    if vals[0] == 'tv_show':
        data_tv = data[data.type == 'tv_show']
        row = data_tv.sample()
        name = row.item.tolist()[0]

    return name

#print(suggest_movie(ARGS, IMDB_DATA))
