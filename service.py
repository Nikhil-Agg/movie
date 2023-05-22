import webapp2
from paste import httpserver

from initialize import Initialize
from routes.movie_routes import MOVIE_ROUTES

import logging
logger = logging.getLogger()

app = webapp2.WSGIApplication(MOVIE_ROUTES, debug=True)

# def main():
#     try:
#         Initialize.initialize_service_startup_dependencies()
#         # httpserver.serve(app, host='127.0.0.1', port='8080')
#         app.run()
#     except Exception as e:
#         logger.exception("Something went wrong while starting service :: error - {}".format(e))

# if __name__ == '__main__':
#     main()
