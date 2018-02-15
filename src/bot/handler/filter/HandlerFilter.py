from abc import ABC, abstractmethod
from bot import Message


class HandlerFilter(ABC):

    @abstractmethod
    def filter(self, message: Message) -> bool:
        pass
