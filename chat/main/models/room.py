from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

ROOM_MODE = [
    (1, 'Conversation'),
    (2, 'Group'),
]

class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_user', blank=False)
    label = models.CharField(max_length=200)
    mode = models.CharField(max_length=1, choices=ROOM_MODE)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return '{} - {}'.format(self.id, self.creator.username)

    def __str__(self):
        return '{} - {}'.format(self.id, self.creator.username)
    
    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
    
        super(Room, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        self.update_at = datetime.now()
    
        super(Room, self).update(*args, **kwargs)

