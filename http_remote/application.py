from tornado.web import StaticFileHandler

from http_remote.handlers import home, mute, play, track, volume
from http_remote.settings import STATIC_DIR


HOME_PATTERN = r'/'
MUTE_PATTERN = r'/mute/?'
PLAY_PATTERN = r'/play/?'
STATIC_PATTERN = r'/static/(.*)'
TRACK_PATTERN = r'/track/?'
VOLUME_PATTERN = r'/volume/?'


handlers = [
    (HOME_PATTERN, home.HomeHandler),
    (MUTE_PATTERN, mute.MuteHandler),
    (PLAY_PATTERN, play.PlayHandler),
    (STATIC_PATTERN, StaticFileHandler, {'path': STATIC_DIR}),
    (TRACK_PATTERN, track.TrackHandler),
    (VOLUME_PATTERN, volume.VolumeHandler),
]
