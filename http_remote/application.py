from http_remote.handlers import volume


VOLUME_PATTERN = r'/volume/?'

handlers = [
    (VOLUME_PATTERN, volume.VolumeHandler),
]
