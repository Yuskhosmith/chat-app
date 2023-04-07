from django.urls import re_path
from . import consumers
# room_name from the urls.py path

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi())
]