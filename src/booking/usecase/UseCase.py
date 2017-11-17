from abc import ABC, abstractmethod


class UseCase(ABC):
    """
    Interface that represents a Generic Use Case.
    """

    @abstractmethod
    def set_request_value(self, value):
        """
        Sets the value used to compute the result.
        :param value: The value that will be used to do the computations.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Performs the computations
        """
        pass

    @abstractmethod
    def get_result_value(self) -> object:
        """
        Gets the result value of the computation.
        :return: Returns the value computed from the use case.
        """
        pass