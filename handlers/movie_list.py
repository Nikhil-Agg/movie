from handlers.base_movie_handler import BaseMovieHandler


class MovieListHandler(BaseMovieHandler):

    IMDB_LINK = "https://www.imdb.com/title/{}"
    TEMPLATE_NAME = "list.html"

    def get(self):
        """Renders list page with title and poster"""
        data = self.fetch_movies_list()
        template = self.get_template_name()
        rendered_data = self.jinja_manager.render_text(template=template, data=data)
        self.response.write(rendered_data)

    def fetch_movies_list(self):
        """Fetches movies from the DB"""
        # data = QueryMovies.query_db()
        # result = {
        #     "movies": []
        # }
        # for _data in data:
        #     _data = self.named_tuple_to_dict(_data)
        #     result["movies"].append(_data)
        for movie in self.data.get("movies"):
            imdb_link = self.IMDB_LINK.format(movie.get("imdbID"))
            movie["imdb_link"] = imdb_link
        return self.data
    
    @staticmethod
    def named_tuple_to_dict(data):
        return {key:getattr(data,key) for key in data._properties if key[0] != '_'}


    def get_template_name(self):
        """Returns template name that is needed to be rendered"""
        # TODO: Change the below logic to remove static template names
        return self.TEMPLATE_NAME
