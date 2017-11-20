import dependency_injector.providers as providers
from .BaseSpider import BaseSpider
from .SpiderEvent import SpiderEvent
from .BuildingsProvider import BuildingsProvider
from .SpiderFactory import SpiderFactory

SpiderFactoryProvider = providers.Singleton(SpiderFactory)
