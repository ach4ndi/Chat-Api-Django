from rest_framework import serializers
from main.serializers.user import UserSerializer
from main.models.room import Room
from main.models.message import Message

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
     
    class Meta:
        model = Message
        fields = ('id', 'user', 'message')