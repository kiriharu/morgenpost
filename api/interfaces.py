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

    @url.getter
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
