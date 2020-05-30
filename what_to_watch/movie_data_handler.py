"""
Provides interface for the data
underpinning the suggestion system
linting saying too few public methods
input output error related to import from db_handler.db_connection_query
"""
import sqlite3
import csv

from .media import MediaItem


EXAMPLE_MEDIA_ITEM = MediaItem(
    title="Space Jam",
    media_type="movie",
    rating=7.0,
    genres="action",
    language="en",
    year=1996,
    num_votes=1000,
    is_adult=False,
)

class MediaItemDataHandler:
    """
    Load, update and select movies
    """
    # pylint: disable=too-few-public-methods,no-self-use

    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: str = 'drama',
            language: str = 'en',
    ) -> MediaItem:
        '''
        Get a random movie that matches the criteria
        '''
        # subset_imdb_data = get_data_from_db(threshold_rating, genre, language)
        # new_media_item = get_media_item(subset_imdb_data)
        return EXAMPLE_MEDIA_ITEM


class SQLLiteMediaItems(MediaItemDataHandler):
    '''
    For use with SQLLite DB
    '''
    def __init__(self, db_name: str = 'imdb.db'):
        super().__init__()
        self.db_name = db_name

    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: str = 'drama',
            language: str = 'en',
    ) -> MediaItem:
        # pylint: disable=unused-argument
        with sqlite3.connect(self.db_name) as conn:
            # TODO: update query with params
            cursor = conn.execute('SELECT * FROM MediaItems ORDER BY RANDOM() LIMIT 1;')
            row = cursor.fetchone()
            cursor.close()

        media_item = MediaItem(*row[1:])    # ignore row id
        media_item.is_adult = bool(media_item.is_adult)
        return media_item

    def update_db_imdb_tems(self, imdb_csv_path: str = 'resources/imdb_data.csv') -> None:
        '''
        Update the DB with new imdb records from
        a specified CSV file
        '''
        with open(imdb_csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            media_items = [
                MediaItem(
                    media_type=row[3],
                    title=row[0],
                    rating=float(row[7]),
                    genres=row[6],
                    language=row[2],
                    year=int(row[5]),
                    num_votes=int(row[-2]),
                    is_adult=bool(row[-1]),
                )
                for i, row in enumerate(reader)
                if i
            ]

        sql_query = """INSERT INTO MediaItems
            (mediaType, title, averageRating, genres, language, year, numVotes, isAdult) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)""" 
        data_tuple = [(
            media_item.media_type,
            media_item.title,
            media_item.rating,
            media_item.genres,
            media_item.language,
            media_item.year,
            media_item.num_votes,
            media_item.is_adult,
        ) for media_item in media_items]
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.executemany(sql_query, data_tuple)
            cursor.close()
            conn.commit()


if __name__ == "__main__":
    handler = SQLLiteMediaItems()
    handler.update_db_imdb_tems()
