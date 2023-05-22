import ast
import logging

import requests

logger = logging.getLogger()

class APIClient:

    @classmethod
    def make_request(cls, method, url, payload=None, headers=None):

        try:
            response = requests.request(method, url, headers=headers, data=payload)
            data = response.content
            print(data)
            data = ast.literal_eval(data)
            return data
        except Exception as e:
            logger.exception("Error while requesting url - {} :: error - {}".format(url, e))
            raise e
