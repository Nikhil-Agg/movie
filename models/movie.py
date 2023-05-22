# from google.cloud import ndb

# import os, sys, inspect

# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

# from handlers.utils import config


# class Movie(ndb.Model):
#     title = ndb.StringProperty()
#     director = ndb.StringProperty()
#     actors = ndb.StringProperty(repeated=True)
#     genre = ndb.StringProperty(repeated=True)
#     imdbID =ndb.StringProperty()
#     imdbLink = ndb.StringProperty()
#     created = ndb.DateTimeProperty(auto_now_add=True)


# class QueryMovies:

#     CLIENT = None

#     @classmethod
#     def initialize_client(cls):
#         if cls.CLIENT is None:
#             cls.CLIENT = ndb.Client(project=config.get("PROJECT_ID"))

#     @classmethod
#     def query_db_with_filter(cls, where_qeury):
#         """
#         where_query = {
#             "genre": [],
#             "actors": [],
#         }
#         """
#         resultant_filter = []
#         if "genre" in where_qeury:
#             resultant_filter.append(Movie.genre.IN(where_qeury.get("genre", [None])))
#         if "actors" in where_qeury:
#             resultant_filter.append(Movie.actors.IN(where_qeury.get("actors", [None])))
#         if "director" in where_qeury:
#             resultant_filter.append(Movie.director==where_qeury.get("director"))
#         print("resultant_filter: ", resultant_filter)
#         with cls.CLIENT.context():
#             result = Movie.query().filter(ndb.AND(*resultant_filter)).fetch()
#             print(result)

#     @classmethod
#     def query_db(cls):
#         if cls.CLIENT is None:
#             cls.initialize_client()
#         with cls.CLIENT.context():
#             return Movie.query().fetch()

#     @classmethod
#     def insert_in_db(cls, title, director, actors, genre, imdbID, imdbLink):
#         with cls.CLIENT.context():
#             movie = Movie(
#                 title=title,
#                 director=director,
#                 actors=actors,
#                 genre=genre,
#                 imdbID=imdbID,
#                 imdbLink=imdbLink
#             )
#             movie.put()

# client = ndb.Client(project="moviefy-387215")
# with client.context():
#     query = Movie.query().filter(ndb.AND(Movie.genre.IN(["action"]))).fetch()
#     print(query)
#     print(query[0].director)
#     print(type(query[0]))



# client = ndb.Client(project="moviefy-387215")
# with client.context():
#     movie = Movie(
#         title="Guardians of the Galaxy Vol. 2".lower(),
#         director="James Gunn".lower(),
#         actors="Chris Pratt, Zoe Saldana, Dave Bautista".lower().split(", "),
#         genre="Action, Adventure, Comedy".lower().split(", "),
#         imdbID="tt3896198",
#         imdbLink="https://www.imdb.com/title/tt3896198"
#     )
#     movie.put()

