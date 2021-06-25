from typing import List, Tuple

import feedparser
import requests
from dataclasses import dataclass

from api.service_apis.interfaces import IApi


class RSSConfig:
    def __init__(self, max_entries: int, feeds: List[Tuple[str, str]]):
        self.max_entries = max_entries
        self.feeds = feeds


@dataclass
class NewsObj:
    link: str
    title: str

    def __str__(self):
        return f"[{self.title}]({self.link})"


class Feed:

    def __init__(self, name, links, max_entries):
        self.name = name
        self.links = links
        self.max_entries = max_entries

    def get(self):
        strings = []
        parsed = feedparser.parse(self.links)
        for field in parsed['entries'][0:self.max_entries]:
            strings.append(NewsObj(
                link=field.get('link'),
                title=field.get('title', 'invalid_title')
            ))

        feed_message = f"🗞 {self.name}\n"
        for entry in strings:
            feed_message += f"📍 {str(entry)}\n"

        feed_message += "\n"
        return feed_message


class RSS(IApi):

    @property
    def url(self):
        return "\n".join(["\n".join([link for link in feed]) for feed in self.feeds])

    @property
    def header(self):
        return "Сводки новостей с RSS:"

    def __init__(self, config: RSSConfig):
        self.feeds = config.feeds
        self.max_entries = config.max_entries

    def get(self):
        rss_message = "Сводка с RSS пуста!"
        if self.max_entries > 0 and len(self.feeds) > 0:
            rss_message = self.header + '\n'
            for feed in self.feeds:
                rss_message += Feed(feed[0], feed[1], self.max_entries).get()

            rss_message += "\n"

        return rss_message
