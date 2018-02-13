from typing import List
from injector import inject

from booking.spider import BaseSpider
from booking.spider.uniweb.math import ArchimedeTowerSpider, LuzzatiSpider, PaolottiSpider


class SpiderFactory:

    @inject
    def __init__(self):
        self._spiders = [ArchimedeTowerSpider(), LuzzatiSpider(), PaolottiSpider()]

    def get_spiders(self) -> List[BaseSpider]:
        return self._spiders
