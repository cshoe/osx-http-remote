import os

VOLUME_UP = """osascript <<END
    set vol to output volume of (get volume settings)
    set vol_interval to 5
    if vol > (100 - vol_interval) then
	set volume output volume 100
    else
	set volume output volume (vol + vol_interval)
    end if
    END"""

VOLUME_DOWN = """osascript <<END
    set vol to output volume of (get volume settings)
    set vol_interval to 5
    if (vol - vol_interval) < 0 then
	set volume output volume 0
    else
	set volume output volume (vol - vol_interval)
    end if
    END"""


def run(cmd):
    """Run an AppleScript using `osascript` the corresponds to `cmd`.

    :param cmd: Name of command to run. Valid values are: 'volume up',
        'volume down'
    :type cmd: string

    :rtype: boolean indicating success or failure

    """
    cmd_map = {
        'volume up': VOLUME_UP,
        'volume down': VOLUME_DOWN
    }

    script = cmd_map.get(cmd, None)
    if script is None:
        return False

    os.system(script)
    return True
