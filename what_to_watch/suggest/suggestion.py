"""
Movie suggestion handling
"""

from .movie_data_handler import MovieDataHandler

def suggest_movie(
        threshold_rating: float = 7.0,
        genre: str = 'drama',
        language: str = 'en',
)-> str:
    '''
    Returns a movie title as a suggestion
    '''
    movie_handler = MovieDataHandler()
    movie_handler.get_random_movie(threshold_rating, genre, language)
    return str(movie_handler.media_item.title)
