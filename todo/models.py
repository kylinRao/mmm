from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from users.models import User
import datetime
class Todo(models.Model):
	user_name = models.ForeignKey(User)
	remind_time = models.TimeField()
	remind_title = models.CharField(max_length=30)
	remind_content = models.CharField(max_length=200)
	remind_only_onece = models.BooleanField()
	remind_receiver_email = models.EmailField()
	remind_sender_email = models.EmailField(default=settings.EMAIL_HOST_USER)
	def __unicode__(self):
		return "{remind_time}_{remind_title}".format(remind_time=self.remind_time,remind_title=self.remind_title)












# Create your models here.
