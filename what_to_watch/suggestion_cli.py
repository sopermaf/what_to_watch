"""
Movie suggestion handling
"""

from .movie_data_handler import MediaItemDataHandler, SQLLiteMediaItems
from .media import MediaItem

def suggest(
        handler: MediaItemDataHandler,
        threshold_rating: float = 7.0,
        genre: str = 'drama',
        language: str = 'en',
    )-> MediaItem:
    '''
    Suggest a MediaItem to watch
    '''
    return handler.get_random_movie(threshold_rating, genre, language)


# TODO: expand with choice detials, local or remote, etc
# include rating, etc
if __name__ == "__main__":
    media_item = suggest(SQLLiteMediaItems())
    print(f"You should watch {media_item.title.capitalize()}")
