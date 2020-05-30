"""
Movie suggestion handling
"""

from .movie_data_handler import MediaItemDataHandler
from .media import MediaItem

def suggest(
        threshold_rating: float = 7.0,
        genre: str = 'drama',
        language: str = 'en',
        handler=MediaItemDataHandler
    )-> MediaItem:
    '''
    Suggest a MediaItem to watch
    '''
    movie_handler = handler()
    suggested_media = movie_handler.get_random_movie(
        threshold_rating,
        genre,
        language
    )
    return suggested_media


# TODO: expand with choice detials
# include rating, etc
if __name__ == "__main__":
    media_item = suggest()
    print(f"You should watch {media_item.title}")
