from booking.spider.uniweb import BaseUniwebSpider
from booking.spider.BuildingsProvider import builder as buildings_provider_builder
from booking.spider import BuildingsProvider


class LuzzatiSpider(BaseUniwebSpider):

    def __init__(self):
        BaseUniwebSpider.__init__(self, '0265-0260B-0260C', 'LUZ')

    def get_buildings_provider(self) -> BuildingsProvider:
        return buildings_provider_builder() \
            .add_building("LUZ", "Luzzati") \
            .add_classroom("LUM250", 1) \
            .add_classroom("LUF1", 1) \
            .add_classroom("LUF2", 1) \
            .add_classroom("LU3", 1) \
            .add_classroom("LU4", 1) \
            .build()


if __name__ == '__main__':
    spider = LuzzatiSpider()
    events = spider.get_events()
    print(events)
