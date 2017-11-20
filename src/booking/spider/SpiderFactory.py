from typing import List
from booking.spider import BaseSpider
from booking.spider.uniweb.math import ArchimedeTowerSpider, LuzzatiSpider, PaolottiSpider


class SpiderFactory:

    def __init__(self):
        self._spiders = [ArchimedeTowerSpider(), LuzzatiSpider(), PaolottiSpider()]

    def get_spiders(self) -> List[BaseSpider]:
        return self._spiders
