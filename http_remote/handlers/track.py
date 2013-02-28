from tornado.web import RequestHandler

from http_remote import applescript


class TrackHandler(RequestHandler):
    """
    Track resource.

    """

    def post(self):
        """
        Go to the next track.

        """
        skipped = applescript.run('next track')
        self.set_status(204) if skipped else self.set_status(500)
        self.write('')


    def delete(self):
        """
        Go to the previous track.

        """
        backed_up = applescript.run('previous track')
        self.set_status(204) if backed_up else self.set_status(500)
        self.write('')
