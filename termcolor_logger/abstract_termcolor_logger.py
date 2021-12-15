from abc import ABC, abstractmethod


class AbstractTermcolorLogger(ABC):
    """Abstract class of the termcolor_logger package"""

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        The basic constructor. Creates a new instance of FancyLog using the specified arguments
        :param *args:
        :param **kwargs:
        :return:
        """

    @abstractmethod
    def create_logger(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        pass
