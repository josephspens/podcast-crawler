import re
from typing import List
import requests
from clients.topic import Topic

PROJECT_ID = "podcast-ingestion"
TOPIC_NAME = "genres"
PODCAST_HOME_URI = "https://podcasts.apple.com/us/genre/podcasts/id26"
TOP_GENRE_PATTERN = r'https:\/\/podcasts\.apple\.com\/us\/genre\/[^\/]+\/id([\d]+)"[^>]+class="top-level-genre'


class Genre:
    def __init__(self):
        self.topic = Topic(PROJECT_ID, TOPIC_NAME)

    def fetch(self) -> List[str]:
        response = requests.get(PODCAST_HOME_URI)
        print(response)
        return re.findall(TOP_GENRE_PATTERN, response.text)

    def publish_all(self, ids: List[str]) -> None:
        self.topic.publish_all_blocking(ids)
