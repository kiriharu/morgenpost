import feedparser
import requests
from dataclasses import dataclass
from config import config


@dataclass
class NewsObj:
    link: str
    title: str

    def __str__(self):
        return f"[{self.title}]({self.link})"


class RSS:

    def __init__(self, name, url):
        self.name = name
        self.feed = requests.get(url).text

    def parse_feed(self):
        news_objects = []

        feed = feedparser.parse(self.feed)
        for field in feed['entries'][0:config.RSS_MAX_ENTRIES]:
            news_objects.append(NewsObj(
                link=field.get('link'),
                title=field.get('title', 'invalid title')
            ))
        return news_objects
