
from django.urls import path

from main.views.user import UserLoginView, UserCreationView, UserProfileView,UserAllProfileView
from main.views.room import RoomUserView

API_PREFIX = 'api'

urlpatterns = [
    path(f'{API_PREFIX}/register/', UserCreationView.as_view()),
    path(f'{API_PREFIX}/login/', UserLoginView.as_view()),
    path(f'{API_PREFIX}/user/', UserProfileView.as_view()),
    path(f'{API_PREFIX}/users/', UserAllProfileView.as_view()),
    path(f'{API_PREFIX}/room/', RoomUserView.as_view()),
]
