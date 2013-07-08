from tornado import template
from tornado.web import RequestHandler

from http_remote.settings import TEMPLATE_DIR



class HomeHandler(RequestHandler):
    """Serve a bootstrap HTML page to get things started.

    """

    def get(self):
        """Serve index.html.

        """
        loader = template.Loader(TEMPLATE_DIR)
        self.write(loader.load('index.html').generate())
