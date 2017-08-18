from typing import List

from .. import BaseSpider
from .. import SpiderEvent
from ..BuildingsProvider import builder as buildings_provider_builder
from .. import BuildingsProvider
from datetime import date
from datetime import time
from datetime import datetime
from lxml import html


def str_to_time(value: str) -> time:
    return datetime.strptime(value, '%H:%M').time()


class MathSpider(BaseSpider):

    def __init__(self):
        BaseSpider.__init__(self, 'http://db1.math.unipd.it/booking/?id_vistarisorsa=9')

    def get_events(self) -> List[SpiderEvent]:
        tree = self._get_html_tree().xpath('//*[@id="squeeze"]/div/div/div[2]/div[1]/ul')  # type: List[html.HtmlElement]
        data = []
        for element in tree:
            if "menu" in element.classes:
                event_times = element[0].xpath('./a/text()')[0].replace(' ', '').split('-')
                location_data = element[2].xpath('./ul[1]/li[1]/text()')[0].split(',')
                class_room = location_data[0]
                build = location_data[2].split(" - ")[1].lower()
                if "paolotti" in build:
                    build = "PAO"
                elif "torre" in build:
                    build = "TA"
                elif "luzzatti" in build:
                    build = "LUZ"
                event_name = element[4].xpath('text()')[0][1:]
                event_desc = element[3].xpath('text()')[0][1:]
                start_time = str_to_time(event_times[0])
                end_time = str_to_time(event_times[1])
                event = SpiderEvent(class_room, build, event_name, event_desc, start_time, end_time, date.today())
                data.append(event)
        return data

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
            .add_building("LUZ", "Luzzati") \
            .add_classroom("LUM250", 1) \
            .add_classroom("LUF2", 1) \
            .add_building("PAO", "Paolotti") \
            .add_classroom("LabP140", 3) \
            .add_classroom("LabP036", 3) \
            .add_classroom("P200", 4) \
            .build()


