from handlers.base_movie_handler import BaseMovieHandler
from handlers.utils import config, convert_unicode_to_dict
from service_clients.api_handler import APIClient


class MovieUploadHandler(BaseMovieHandler):

    RESULTANT_TEMPLATE_NAME = "list.html"
    FORM_TEMPLATE_NAME = "upload_form.html"
    ERROR_TEMPLATE = "404.html"
    IMDB_LINK = "https://www.imdb.com/title/{}"

    def get(self):
        template = self.FORM_TEMPLATE_NAME
        rendered_data = self.jinja_manager.render_text(template=template, data={})
        self.response.write(rendered_data)

    def post(self):
        title = self.request.POST["title"]
        movie_data = self.get_data_from_imdb(title=title)
        if movie_data.get("Error"):
            rendered_data = self.jinja_manager.render_text(template=self.ERROR_TEMPLATE, data={})
            self.response.write(rendered_data)
            return
        print("movie data: ", movie_data)
        print(type(movie_data))
        movie_data = self.add_imdb_link(movie_data=movie_data)
        self.data.get("movies", []).append(movie_data)
        template = self.RESULTANT_TEMPLATE_NAME
        print(self.data.get("movies"))
        rendered_data = self.jinja_manager.render_text(template=template, data=self.data)
        self.response.write(rendered_data)

    @staticmethod
    def get_data_from_imdb(title=''):
        imdb_config = config.get("IMDB", {})
        api_key = imdb_config.get("API_KEY")
        url = imdb_config.get("SEARCH_URL").format(title=title, api_key=api_key)
        return APIClient.make_request(method="GET", url=url)
    
    def add_imdb_link(self, movie_data):
        print(movie_data)
        print(type(movie_data))
        imdb_link = self.IMDB_LINK.format(movie_data.get("imdbID"))
        movie_data["imdb_link"] = imdb_link
        return movie_data
