from abc import ABCMeta, abstractmethod, abstractproperty

from typing import Union


class ISocialNet:
    __metaclass__ = ABCMeta

    @abstractmethod
    def call(self, method: str, params: dict) -> dict:
        """Call API method"""
        raise NotImplementedError

    @abstractmethod
    def send_message(self, chat_id: Union[str, int], text: str) -> dict:
        """Send message to chat"""
        raise NotImplementedError

    @abstractmethod
    def send(self, text: str, chat_id: Union[str, int]) -> None:
        """Safety send message to chat"""
        raise NotImplementedError

    @property
    @abstractmethod
    def api_url(self):
        """API's url"""
        raise NotImplementedError
