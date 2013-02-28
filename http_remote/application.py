from http_remote.handlers import mute, play, track, volume


MUTE_PATTERN = r'/mute/?'
PLAY_PATTERN = r'/play/?'
TRACK_PATTERN = r'/track/?'
VOLUME_PATTERN = r'/volume/?'

handlers = [
    (MUTE_PATTERN, mute.MuteHandler),
    (PLAY_PATTERN, play.PlayHandler),
    (TRACK_PATTERN, track.TrackHandler),
    (VOLUME_PATTERN, volume.VolumeHandler),
]
