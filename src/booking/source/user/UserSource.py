from abc import ABC
from abc import abstractmethod
from .User import User
from typing import List


class UserSource(ABC):
    """
    Class that represents a source used to store and get the user that use the bot.
    """

    @abstractmethod
    def get_user_by_identifier(self, identifier: int) -> User:
        """
        Gets the user that have the identifier equal to the provided identifier.
        :param identifier: Identifier used to get the user.
        :return: Return the user that have the requested identifier, if the user is not present will return None.
        """
        pass

    def get_all_users(self) -> List[User]:
        """
        Gets all the users.
        :return: Return a list of all the users.
        """
        pass

    def add_user(self, user: User):
        """
        Adds a user.
        :param user: User that will be added.
        :return:
        """
        pass
