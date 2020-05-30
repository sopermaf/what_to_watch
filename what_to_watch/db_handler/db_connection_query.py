"""
file which will have methods to push,pull data from database table set up on azure
"""
import pandas as pd
import pyodbc

from suggest.media_item import MediaItem

SERVER = 'fitbit-fizzyo-test.database.windows.net'
DATABASE = 'fitbit_data'
USERNAME = 'kapoork'
PASSWORD = 'ferd_kunal_project_2020'
DRIVER = '{SQL Server}'

def get_data_from_db(threshold_rating: float, genre: str, language: str) -> pd.DataFrame:
    '''
    function that returns data from sql database
    where the imdb_data is stored in a pandas data frame
    data returned is based on the query passed
    '''
    cnxn = pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER+
    ';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)

    sql_str = "SELECT * FROM imdb_data where genre LIKE (?) and rating > (?) and language = (?)"
    genre = '%' + genre + '%'
    subset_imdb_data = pd.read_sql_query(sql_str, cnxn, params=(genre, threshold_rating, language))
    cnxn.close()
    return subset_imdb_data

def get_media_item(subset_imdb_data: pd.DataFrame) -> MediaItem:
    '''
    takes pandas dataframe returned by the get_data_from_db function,
    chooses a random row, then maps to a Media_item and returns
    '''
    if len(subset_imdb_data) > 0:
        random_media_item = subset_imdb_data.sample()
        new_media_item = row_to_media_item(random_media_item)
    else:
        new_media_item = MediaItem('space jam', 'movie', '6', 'comedy', 'en', 1996, 18000, 0)
    return new_media_item

def row_to_media_item(random_row: pd.DataFrame) -> MediaItem:
    '''
    convert imdb data row to media_item
    '''
    new_media_item = MediaItem(random_row['title'].values[0], random_row['titleType'].values[0],
    random_row['rating'].values[0], random_row['genre'].values[0], random_row['language'].values[0], 
    random_row['year'].values[0], random_row['num_votes'].values[0],
    random_row['is_adult'].values[0])
    return new_media_item
