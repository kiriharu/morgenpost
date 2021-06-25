from abc import abstractmethod, ABC


class IApi(ABC):

    @abstractmethod
    def get(self, *args, **kwargs) -> str:
        """Get info from API"""
        raise NotImplementedError

    @property
    @abstractmethod
    def url(self):
        """API's url"""
        raise NotImplementedError

    @property
    @abstractmethod
    def header(self):
        """API's header"""
        raise NotImplementedError
