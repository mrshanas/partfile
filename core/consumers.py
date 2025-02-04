import json

from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

from .read import chunk_file_read

class FileConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        try:
            data = json.loads(text_data)
            page = data.get('page', 1)

            result = chunk_file_read(page, settings.LARGE_FILE_PATH)
            self.send(text_data = json.dumps(result))

        except Exception as e:
            print(e)