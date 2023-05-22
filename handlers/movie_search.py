from handlers.base_movie_handler import BaseMovieHandler
from handlers.utils import convert_unicode_to_dict


class MovieSearchHandler(BaseMovieHandler):
    """Class to handle movie search requests"""

    RESULTANT_TEMPLATE_NAME = "list.html"
    FORM_TEMPLATE_NAME = "search_form.html"

    def get(self):
        template = self.FORM_TEMPLATE_NAME
        rendered_data = self.jinja_manager.render_text(template=template, data={})
        self.response.write(rendered_data)

    def post(self):
        """Takes a post request and renders the webpage with filtered movie data"""
        data = self.request.POST.items()
        where_qeury = convert_unicode_to_dict(data=data)
        search_movie_result = self.search_movie(where_query=where_qeury)
        template = self.RESULTANT_TEMPLATE_NAME
        rendered_data = self.jinja_manager.render_text(template=template, data=search_movie_result)
        self.response.write(rendered_data)

    def search_movie(self, where_query):
        """
        Searches movies data with the given filter
        Parameter
        ---------
            where_query: dict
                where filter for querying database
                    e.g.
                        {
                            'Director': 'James Gunn', 
                            'Genre': 'Action, Adventure, Comedy'
                        }
        
        Returns
        -------
            search_movie_result: dict
                Returns movie details filtered with the given query
                    
        """
        # TODO: Need to change with db
        search_movie_result = {"movies": []}
        for movie in self.data.get("movies"):
            for field in where_query:
                if where_query[field] and where_query[field] in movie[field]:
                    search_movie_result['movies'].append(movie)

        return search_movie_result
