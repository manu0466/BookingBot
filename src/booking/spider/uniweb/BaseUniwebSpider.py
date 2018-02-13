from typing import List

from booking.spider import BaseSpider
from booking.spider import SpiderEvent
from datetime import date
from datetime import time
from datetime import datetime
import requests
import json
import logging


def str_to_time(value: str) -> time:
    return datetime.strptime(value, '%H:%M:%S').time()


class BaseUniwebSpider(BaseSpider):

    def __init__(self, building_id: str, building_key: str):
        """
        Default constructor
        :param building_id: the id associated from the site to the building.
        :param building_key: the key associated to the building created using the BuildingBuilder.
        """
        BaseSpider.__init__(self, 'http://gestionedidattica.unipd.it/PortaleStudenti/rooms_call.php')
        self._building_id = building_id
        self._building_key = building_key

    def get_events(self) -> List[SpiderEvent]:
        payload = {'form-type': 'rooms',
                   'sede': self._building_id,
                   'date': datetime.now().strftime("%d-%m-%Y"),
                   '_lang': 'it',
                   }
        response = requests.post(self._get_url(), payload)
        result = []
        if response.status_code == 200:
            data = json.loads(response.text)
            if data['n_events'] > 0:
                events = data['events']
                for event in events:
                    name = event['name']
                    start = event['from']
                    end = event['to']
                    classroom = event['NomeAula']
                    building = event['NomeSede']
                    logging.info(name + " " + start + "-" + end + " " + classroom + " " + building)
                    result.append(SpiderEvent(classroom, self._building_key, name, "", str_to_time(start), str_to_time(end),
                                              date.today()))
        else:
            logging.error(response.content)
        return result


if __name__ == '__main__':
    spider = BaseUniwebSpider("306", "")
    events = spider.get_events()
    print(events)
