"""
file which will have methods to push,pull data from database table set up on azure
"""
import pyodbc
import pandas as pd
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from what_to_watch.suggest.media_item import Media_item

SERVER = '###'
DATABASE = '###'
USERNAME = 'kapoork'
PASSWORD = '###'
DRIVER= '{SQL Server}'

def get_conn():
    '''
    function that returns connection to the sql database where the imdb_data is stored
    '''
    cnxn = pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
    return cnxn

def get_media_item(threshold_rating: float, genre: str, language: str) -> Media_item:
    '''
    pulls filtered data from db table, places in pandas dataframe
    chooses a random row, then maps to a Media_item and returns
    '''
    sql_str = "SELECT * FROM imdb_data where genre LIKE (?) and rating > (?) and language = (?)"
    genre = '%' + genre + '%'
    cnxn = get_conn()
    subset_imdb_data = pd.read_sql_query(sql_str, cnxn,params = (genre,threshold_rating,language))
    cnxn.close()

    random_media_item = subset_imdb_data.sample()
    new_media_item = row_to_media_item(random_media_item)
    return new_media_item

def row_to_media_item(random_row: pd.DataFrame) -> Media_item:
    '''
    convert imdb data row to media_item
    '''
    new_media_item = Media_item(random_row['title'].values[0],random_row['titleType'].values[0],random_row['rating'].values[0],
    random_row['genre'].values[0],random_row['language'].values[0],random_row['year'].values[0],
    random_row['num_votes'].values[0],random_row['is_adult'].values[0])
    return new_media_item

#python DB_handler/db_connection_query.py