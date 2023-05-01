import os
import requests
from googleapiclient.discovery import build
api_key = os.getenv('YT_API_KEY')

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey="AIzaSyAAFIjHIkwcu7HPEs_7sCje4Aa4LvyPAOQ")
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
