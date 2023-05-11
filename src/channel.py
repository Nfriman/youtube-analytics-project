import json
import os
from googleapiclient.discovery import build
api_key = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        youtube = build('youtube', 'v3', developerKey=api_key)
        self.info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA'
        self.subscriber_count = self.info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.info['items'][0]['statistics']['videoCount']
        self.view_count = self.info['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)

    def to_json(self, json_file):
        data = {
            "id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count

        }

        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return data

    @classmethod
    def get_service(cls):
        """возвращающий объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
