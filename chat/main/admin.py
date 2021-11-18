from django.contrib import admin

# Register your models here.
from main.models.message import Message
from main.models.room import Room
from main.models.room_user import RoomUser

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('room', 'user', 'message', 'created_at', 'update_at')

class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ('creator', 'label', 'mode', 'created_at', 'update_at')

class RoomUserdmin(admin.ModelAdmin):
    model = RoomUser
    list_display = ('room', 'attendant', 'unread_count', 'created_at', 'update_at')

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomUser, RoomUserdmin)
admin.site.register(Message, MessageAdmin)