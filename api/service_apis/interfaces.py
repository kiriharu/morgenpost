from abc import ABCMeta, abstractmethod, abstractproperty


class IApi:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, *args, **kwargs) -> str:
        """Get info from API"""

    @property
    @abstractmethod
    def url(self):
        """API's url"""
        raise NotImplementedError

    @property
    @abstractmethod
    def header(self):
        """API's url"""
        raise NotImplementedError
