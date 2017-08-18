from . import MathSpider
import os


class OfflineSpider(MathSpider):
    def __init__(self):
        MathSpider.__init__(self)

    def _get_html(self):
        path = os.path.dirname(__file__)
        data = ''
        with open(path + '/offline.html', 'r') as content_file:
            data = content_file.read()
        return data

