from abc import ABCMeta, abstractmethod, abstractproperty

from typing import Union


class ISocialNet:
    __metaclass__ = ABCMeta

    @abstractmethod
    def call(self, method: str, params: dict) -> dict:
        """Call API method"""

    @abstractmethod
    def send_message(self, chat_id: Union[str, int], text: str) -> dict:
        """Send message to chat"""

    @abstractmethod
    def send(self, text: str, chat_id: Union[str, int]) -> None:
        """Safety send message to chat"""

    @property
    @abstractmethod
    def api_url(self):
        """API's url"""

    @api_url.getter
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, value):
        self._api_url = value