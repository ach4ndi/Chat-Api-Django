from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from main.serializers.user import UserSerializer
from main.serializers.room import RoomUserListSerializer
from main.models.room import Room
from main.models.room_user import RoomUser
from django.db.models import Count

class RoomUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = RoomUserListSerializer

    def get_queryset(self):
        user =  self.request.user
        room_list = RoomUser.objects.filter(attendant=user).values_list('room__id').distinct()

        output = []
        
        for data in room_list:
            room_data = Room.objects.get(id=data)
            room_label = user.username + ' with '
            room_user_in = RoomUser.objects.filter(id=data)
            room_user_count = 0
            
            for user_room in room_user_in:
                if user_room.attendant == user:
                    room_user_count = user_room.attendant.unread_count
                    continue
                room_label += user_room.attendant.username
        
            insert_data = {
                'id' : room_data.id,
                'creator' : UserSerializer(room_data.creator),
                'label' : room_label + f' {room_user_count}',
                'unread_count' : room_user_count
            }
            
            output.append(insert_data)
        
        return output

class RoomCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request, *args, **kwargs):
        user =  self.request.user
        user_target = User.Objects.get(id=request.data['target_id'])
        message = request.data['message']
        user_ids = [user.id,user_target.id]
        
        room_find = RoomUser.object.filter(id__in=user_ids).annotate(total=Count('room')).order_by('total').all()
        
        if len(room_find) > 0:
            return {
                'Error' : 'Room is already created'
            }
        
        new_room = Room.objects.create(creator=user,label=user.username + ' with ' + user_target.username, mode=1)
        
        for user_id in user_ids:
            RoomUser.objects.create(room=new_room,attendant__id=user_id)
        
        