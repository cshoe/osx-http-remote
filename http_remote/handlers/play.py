from tornado.web import RequestHandler

from http_remote import applescript


class PlayHandler(RequestHandler):
    """
    Play/pause resource.

    """

    def post(self):
        """
        Go to the next track.

        """
        play_toggled = applescript.run('play pause')
        self.set_status(204) if play_toggled else self.set_status(500)
        self.write('')
