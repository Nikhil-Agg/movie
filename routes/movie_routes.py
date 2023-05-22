import webapp2

from handlers.movie_list import MovieListHandler
from handlers.movie_search import MovieSearchHandler
from handlers.movie_upload import MovieUploadHandler
from handlers.utils import config

MOVIE_ROUTES = [
   webapp2.Route(r'/', handler=MovieListHandler, name='home', methods=['GET']),
   webapp2.Route(r'/search/movie', handler=MovieSearchHandler, name='search'),
   webapp2.Route(r'/upload/movie', handler=MovieUploadHandler, name='upload'),
]
