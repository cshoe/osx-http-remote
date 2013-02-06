from tornado.web import RequestHandler

from http_remote import applescript


class VolumeHandler(RequestHandler):
    """
    Volume resource.

    """

    def get(self):
        """
        Get the current system volume.

        """
        pass

    def post(self):
        """
        Turn up the current system volume.

        """
        turned_up = applescript.run('volume up')
        self.set_status(204) if turned_up else self.set_status(500)
        self.write('')

    def delete(self):
        """
        Turn down the current system volume.

        """
        turned_down = applescript.run('volume down')
        self.set_status(204) if turned_down else self.set_status(500)
        self.write('')
