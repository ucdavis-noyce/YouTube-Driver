import subprocess
import re
import json
from yt_dlp import YoutubeDL

class VideoMetadata:
    def __init__(self, video_json):
        self.id = video_json['id']
        self.title = video_json['title']
        self.webpage_url = video_json['webpage_url']
        self.duration = video_json['duration']
        self.thumbnail = video_json['thumbnail']
        self.description = video_json['description']
        self.upload_date = video_json['upload_date']
        self.channel_id = video_json['channel_id']
        self.channel_url = video_json['channel_url']
        self.age_limit = video_json['age_limit']
        self.channel_name = video_json['uploader']
        self.view_count = video_json['view_count']
        self.like_count = video_json['like_count']
        self.comment_count = video_json['comment_count']
        self.average_rating = video_json['average_rating']
        self.categories = video_json['categories']
        self.tags = video_json['tags']
        self.subtitles = self.__get_subtitles(video_json)
        self.automated_captions = self.__get_automatic_captions(video_json)
        self.video_json = video_json

    def __get_subtitles(self, js):
        subtitles = js.get('subtitles', {})
        if 'en' not in subtitles:
            return None
        return subtitles['en'][0]['url']

    def __get_automatic_captions(self, js):
        captions = js.get('automatic_captions', {})
        if 'en' not in captions:
            return None
        return captions['en'][0]['url']


class VideoUnavailableException(Exception):
    """
    Exception thrown when a played video is private/deleted/copyright struck.
    """
    pass


class Video:
    YT_DLP = YoutubeDL(dict(
        quiet=True
    ))

    def __init__(self, elem, url):
        self.elem = elem
        self.url = url
        self.videoId = re.search(r'[?&]v=(.*)?$', url).group(1).split('&')[0]
        self.__metadata = None

    def get_metadata(self) -> VideoMetadata:
        """
        Get video metadata using `yt-dlp`.
        """
        if not self.__metadata:
            self.__metadata = Video.YT_DLP.extract_info(self.url, download=False)
        return VideoMetadata(self.__metadata)

