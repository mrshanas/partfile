# from django.conf import settings

# with open(settings.BASE_DIR+'100mb-examplefile.txt', 'rb') as f:
#     memoryview(f)

from django.urls import path
from .consumers import FileConsumer

websocket_urlpatterns = [
    path('ws/file-reader', FileConsumer.as_asgi())
]