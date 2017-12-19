from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class ElfManager(models.Manager):
    pass
    # def validate(self, post_data):
    #     errors = []
    #     if len(post_data['tasks']) < 2: 
    #         errors.append("tasks must not be empty")            
    #     if len(post_data['date']) < 1:
    #         errors.append("date must be current or future")
    #     return errors

    # def validate_create(self, post_data):
    #     errors = []
    #     if len(post_data['tasks']) < 2:
    #         errors.append("taska must not be empty")
    #     if len(post_data['time']) < 1:
    #         errors.append("time must not be empty")
    #     if len(post_data['date']) < 1:
    #         errors.append("date must be current or future")
    #     return errors
            
    
class Elf(models.Model):
    elf_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    sponsored = models.ManyToManyField(User, related_name="sponsorer")
    objects = ElfManager()