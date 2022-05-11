import subprocess
import re
import json

class Video:
    def __init__(self, elem, url):
        self.elem = elem
        self.url = url
        self.videoId = re.search(r'\?v=(.*)?$', url).group(1).split('&')[0]
        self.metadata = None

    def get_metadata(self):
        """
        Get video metadata using `youtube-dl`.
        """
        if self.metadata is None:
            proc = subprocess.run(['./youtube-dl', '-J', self.url], stdout=subprocess.PIPE)
            self.metadata = json.loads(proc.stdout.decode())
        return self.metadata


class VideoUnavailableException(Exception):
    """
    Exception thrown when a played video is private/deleted/copyright struck.
    """
    pass


def time2seconds(s):
    """
    Converts a given time (video duration, ad time, etc.) to seconds
    """
    s = s.split(':')
    s.reverse()
    wait = 0
    factor = 1
    for t in s:
        wait += int(t) * factor
        factor *= 60
    return wait
