from handlers.jinja import JinjaManager

# from models.movie import QueryMovies

class Initialize:

    @classmethod
    def initialize_service_startup_dependencies(cls):
        JinjaManager.set_jinja_environment()
        # QueryMovies.initialize_client()
