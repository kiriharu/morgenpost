from abc import ABCMeta, abstractmethod


class IApi:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, *args, **kwargs) -> str:
        """Get info from API"""
