from tornado.web import RequestHandler

from http_remote import applescript


class MuteHandler(RequestHandler):
    """
    Mute resource

    """

    def post(self):
        """
        Toggle mute on/off.

        """
        muted = applescript.run('mute toggle')
        self.set_status(204) if muted else self.set_status(500)
        self.write('')
