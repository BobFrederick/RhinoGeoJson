from geojsontools import geojson
from urllib import request, parse

class Reader():
    """
    Provides methods for opening a GeoJSON via file or url
    """
    def __init__(self, url = None, filepath = None):
        if url:
            self.data = self.from_url(url)
        elif filepath:
            pass

    @classmethod
    def from_url(cls, url):
        """ Reads GeoJSON from a url """
        if cls._validate_url(url):
            with request.urlopen(url) as file:
                data = geojson.load(file)
            return data

    @staticmethod
    def _validate_url(url):
        """ Validates a url string """
        result = parse.urlparse(url)
        if result.scheme and result.netloc:
            return True
