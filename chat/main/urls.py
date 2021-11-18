
from django.urls import path

from main.views.user import UserLoginView, UserCreationView, UserProfileView,UserAllProfileView
from main.views.room import RoomUserView, RoomCreateView
from main.views.message import MessageSendView

API_PREFIX = 'api'

urlpatterns = [
    path(f'{API_PREFIX}/register/', UserCreationView.as_view()),
    path(f'{API_PREFIX}/login/', UserLoginView.as_view()),
    path(f'{API_PREFIX}/user/', UserProfileView.as_view()),
    path(f'{API_PREFIX}/users/', UserAllProfileView.as_view()),
    path(f'{API_PREFIX}/room/', RoomUserView.as_view()),
    path(f'{API_PREFIX}/room/create', RoomCreateView.as_view()),
    path(f'{API_PREFIX}/message/create', MessageSendView.as_view()),
]
