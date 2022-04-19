import subprocess
import re
import json

class Video:
    def __init__(self, elem, url):
        self.elem = elem
        self.url = url
        self.videoId = re.search(r'\?v=(.*)?$', url).group(1).split('&')[0]
        self.metadata = {}

    def get_metadata(self):
        proc = subprocess.run(['./youtube-dl', '-J', self.url], stdout=subprocess.PIPE)
        self.metadata = json.loads(proc.stdout.decode())


class VideoUnavailableException(Exception):
    pass


def time2seconds(s):
    s = s.split(':')
    s.reverse()
    wait = 0
    factor = 1
    for t in s:
        wait += int(t) * factor
        factor *= 60
    return wait
