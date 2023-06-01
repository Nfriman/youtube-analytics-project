import json
import os
from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  # id канала

        youtube = build('youtube', 'v3', developerKey=api_key)
        self.info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        self.title = self.info['items'][0]['snippet']['title']  # Название каннала
        self.description = self.info['items'][0]['snippet']['description']  # Описание канала
        self.url = 'https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA'  # Ссылка на канал
        self.subscriber_count = self.info['items'][0]['statistics']['subscriberCount']  # Количество подписчиков
        self.video_count = self.info['items'][0]['statistics']['videoCount']  # Количество видио
        self.view_count = self.info['items'][0]['statistics']['viewCount']  # Общее количество подписчиков

    def __str__(self):
        """Возврошает название и ссылку на канал"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Суммирует количество подписчиков"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Вычитает количество подписчиков"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __ne__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

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
