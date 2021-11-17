from rest_framework import serializers
from main.serializers.user import UserSerializer
from main.models.room import Room
from main.models.room_user import RoomUser

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'label', 'model')

class RoomUserSerializer(serializers.ModelSerializer):
    attendant = UserSerializer(many=False)
    room = RoomSerializer(many=False)
    
    class Meta:
        model = RoomUser
        fields = ('id', 'room', 'attendant', 'unread_count')