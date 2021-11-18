from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from main.serializers.user import UserSerializer
from main.serializers.room import RoomUserListSerializer, RoomSerializer
from main.models.room import Room
from main.models.room_user import RoomUser
from main.models.message import Message
from django.db.models import Count

class RoomUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        user =  self.request.user
        room_list = RoomUser.objects.filter(attendant=user).values_list('room__id').distinct()

        output = []
        
        for data in room_list:
            room_data = Room.objects.get(id=data[0])
            room_label = user.username + ' with '
            room_user_in = RoomUser.objects.filter(id=data[0])
            room_user_count = 0
            
            for user_room in room_user_in:
                if user_room.attendant == user:
                    room_user_count = user_room.attendant.unread_count
                    continue
                room_label += user_room.attendant.username
        
            insert_data = {
                'id' : room_data.id,
                'creator' : UserSerializer(room_data.creator).data,
                'label' : room_label + f' {room_user_count}',
                'unread_count' : room_user_count
            }
            
            output.append(insert_data)
        
        return Response({
            'status': 200,
            'result': output
            })

class RoomCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request, *args, **kwargs):
        user_main =  self.request.user
        user_target = User.objects.get(id=request.data['target_id'])
        user_ids = [user_main.id,user_target.id]
        
        room_find = RoomUser.objects.filter(id__in=user_ids).annotate(total=Count('room')).order_by('total').values('room').distinct().all()

        if len(room_find) > 0:
            room_field = []
            
            for data in room_find:
                room_field.append(data['room'])
            
            room_query_field = Room.objects.filter(id__in=room_field)
            
            return Response({
                'status': 200,
                'create_new': False,
                'room': RoomSerializer(room_query_field, many=True).data
            })
        
        new_room = Room(creator=user_main,label=user_main.username + ' with ' + user_target.username, mode=1)
        new_room.save()
        
        for user_id in user_ids:
            ruser = RoomUser(room=new_room,attendant=User.objects.get(id=user_id))
            ruser.save()
        
        return Response({
            'status': 200,
            'create_new': True,
            'room': RoomSerializer(new_room, many=True).data
        })