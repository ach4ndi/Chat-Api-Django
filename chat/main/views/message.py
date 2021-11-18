from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from main.serializers.user import UserSerializer
from main.serializers.room import RoomUserListSerializer, RoomSerializer
from main.serializers.message import MessageSerializer
from main.models.room import Room
from main.models.room_user import RoomUser
from main.models.message import Message
from django.db.models import Count

class MessageSendView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    # User send message to other user when the user is listed on room user list
    
    def post(self, request, *args, **kwargs):
        user_main =  self.request.user
        room_id_ip = request.data['room_id']
        message = request.data['message']
        
        room_find = RoomUser.objects.filter(room__id=room_id_ip,attendant=user_main).annotate(total=Count('room')).order_by('total').all()
        
        if len(room_find) == 0:
            return Response({
                'error': 'User Not found on this room user list, you denied send message on this room.'
            })
        
        room_target = Room.objects.get(id=room_id_ip)
        
        msg = Message(room=room_target,message=message,user=user_main)
        msg.save()
        
        room_count = RoomUser.objects.filter(room__id=room_id_ip)
        
        for data in room_count:
            if not data.attendant == user_main:
                data.unread_count +=1
                data.save()
        
        return Response({
                'status': 200,
                'result': MessageSerializer(msg).data
            })

class MessageRoomListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    # When user list message from on their room, their unread count will reset 0
    
    def get(self, request):
        user =  self.request.user
        room_id_ip = request.data['room_id']
        
        room_find = RoomUser.objects.filter(room__id=room_id_ip,attendant=user).annotate(total=Count('room')).order_by('total').all()
        
        if len(room_find) == 0:
            return Response({
                'status': 400,
                'result': []
            })
        
        message_list = Message.objects.filter(room__id=room_id_ip).all()
        
        roomuser_count = RoomUser.objects.get(room__id=room_id_ip,attendant=user)
        roomuser_count.unread_count = 0
        roomuser_count.save()
        
        return Response({
                'status': 200,
                'result': {
                    'room_id': room_id_ip,
                    'messages': MessageSerializer(message_list, many=True).data
                }
            })