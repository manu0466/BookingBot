import abc
from abc import ABCMeta
from typing import List

import requests
from lxml import html
from .BuildingsProvider import BuildingsProvider

from booking.spider.SpiderEvent import SpiderEvent


class BaseSpider(metaclass=ABCMeta):

    """
    Abstract class that represents a spider that collects events from internet.
    """

    def __init__(self, url: str):
        """
        Default constructor
        :param url: The url of the page that contains the events data.
        """
        self._url = url

    @abc.abstractclassmethod
    def get_events(self) -> List[SpiderEvent]:
        """
        This method should return an array of SpiderEvent.
        :return: Returns a List[SpiderEvent] that contains the events obtained from the spider.
        """
        pass

    @abc.abstractclassmethod
    def get_buildings_provider(self) -> BuildingsProvider:
        """
        This method should return a non null instance of BuildingsProvider, that contains the classrooms
        and buildings managed from the spider.
        :return: Return a BuildingsProvider instance.
        """
        pass

    def _get_html(self) -> str:
        """
        Utility function that can be used to extract the html text of the page.
        :return: Returns the text representation of the page at the url provided in the constructor.
        """
        data = ''
        if self._url != '':
            page = requests.get(self._url)
            data = page.content
        else:
            print('Remote url not defined')
        return data

    def _get_html_tree(self) -> html.HtmlElement:
        """
        Gets html of the page as a tree, this can be used to extract the data using some xpath expressions.
        :return: Returns the root of the html tree.
        """
        return html.fromstring(self._get_html())

    def _get_url(self) -> str:
        return self._url
