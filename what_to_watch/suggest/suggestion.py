"""
Movie suggestion handling
"""

from .movie_data_handler import MediaItemDataHandler
from .media import MediaItem

def suggest(
        threshold_rating: float = 7.0,
        genre: str = 'drama',
        language: str = 'en',
    )-> MediaItem:
    '''
    Suggest a MediaItem to watch
    '''
    movie_handler = MediaItemDataHandler()
    media_item = movie_handler.get_random_movie(
        threshold_rating,
        genre,
        language
    )
    return media_item


# TODO: expand with choice detials
# include rating, etc
if __name__ == "__main__":
    media_item = suggest()
    print(f"You should watch {media_item.title}")
