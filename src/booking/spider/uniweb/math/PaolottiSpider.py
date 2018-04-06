from datetime import datetime, timedelta

from booking.spider.uniweb import BaseUniwebSpider
from booking.spider.BuildingsProvider import builder as buildings_provider_builder
from booking.spider import BuildingsProvider


class PaolottiSpider(BaseUniwebSpider):

    def __init__(self):
        BaseUniwebSpider.__init__(self, '0260A', 'PAO')

    def get_buildings_provider(self) -> BuildingsProvider:
        return buildings_provider_builder() \
            .add_building("PAO", "Paolotti") \
            .add_classroom("P1", 1) \
            .add_classroom("P2", 1) \
            .add_classroom("P3", 1) \
            .add_classroom("P4", 1) \
            .add_classroom("P5", 1) \
            .add_classroom("P6", 1) \
            .add_classroom("LabP140", 3) \
            .add_classroom("LabP036", 3) \
            .add_classroom("P200", 4) \
            .add_classroom("P100", 4) \
            .build()


if __name__ == '__main__':
    spider = PaolottiSpider()
    for date in map(lambda i: datetime.today() + timedelta(days=i), range(1, 8)):
        events = spider.get_events(date)
        print(events)
