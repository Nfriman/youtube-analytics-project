import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
api_key = os.getenv('YT_API_KEY')

class Video:

    def __init__(self, video_id):
        self.video_id = video_id  # id video

        try:
            youtube = build('youtube', 'v3', developerKey=api_key)
            self.info = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.url = f"https://www.youtube.com/watch?v={video_id}"  # Ссылка на видео

            self.title = self.info['items'][0]['snippet']['title']  # Название видео
            self.url = f"https://www.youtube.com/watch?v={video_id}"  # Ссылка на видео
            self.view_count: int = self.info['items'][0]['statistics']['viewCount']  # количество просмотров
            self.like_count: int = self.info['items'][0]['statistics']['likeCount']  # количество лайков


        except IndexError:

            self.info = None
            self.url = None
            self.title = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return self.title

class PLVideo(Video):

    def __init__(self, video_id, play_list):
        super().__init__(video_id)
        self.play_list = play_list



