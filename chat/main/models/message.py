from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from main.models.room import Room
from datetime import datetime

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='roommsgs_id', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usermsg_id', blank=False)
    message = models.CharField(max_length=512)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return 'Room {} - [{}] {}'.format(self.room.id, self.id, self.user.username)

    def __str__(self):
        return 'Room {} - [{}] {}'.format(self.room.id, self.id, self.user.username)
    
    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
    
        super(Message, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        self.update_at = datetime.now()
    
        super(Message, self).update(*args, **kwargs)