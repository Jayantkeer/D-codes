from django.urls import path
from .import consumers

websocket_urlpatterns=[
    path('ws/sc/<str:gre>/',consumers.MySyncConsumer.as_asgi()),
]