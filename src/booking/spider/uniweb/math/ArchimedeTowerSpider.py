from booking.spider.uniweb import BaseUniwebSpider
from booking.spider.BuildingsProvider import builder as buildings_provider_builder
from booking.spider import BuildingsProvider


class ArchimedeTowerSpider(BaseUniwebSpider):

    def __init__(self):
        BaseUniwebSpider.__init__(self, '306', 'TA')

    def get_buildings_provider(self) -> BuildingsProvider:
        return buildings_provider_builder() \
            .add_building("TA", "Torre archimede") \
            .add_classroom("1A150", 1) \
            .add_classroom("1AD100", 1) \
            .add_classroom("1BC45", 1) \
            .add_classroom("1BC50", 1) \
            .add_classroom("1C150", 1) \
            .add_classroom("2AB40", 2) \
            .add_classroom("2AB45", 2) \
            .add_classroom("2BC30", 2) \
            .add_classroom("2BC60", 2) \
            .add_classroom("LabTA", 2) \
            .build()


if __name__ == '__main__':
    spider = ArchimedeTowerSpider()
    events = spider.get_events()
    print(events)
