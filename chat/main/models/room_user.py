from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from main.models.room import Room
from datetime import datetime

class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_id', blank=False)
    attendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendant_id', blank=False)
    unread_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return 'Room {} - [{}] {}'.format(self.room.id, self.id, self.attendant.username)

    def __str__(self):
        return 'Room {} - [{}] {}'.format(self.room.id, self.id, self.attendant.username)
    
    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
    
        super(RoomUser, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        self.update_at = datetime.now()
    
        super(RoomUser, self).update(*args, **kwargs)