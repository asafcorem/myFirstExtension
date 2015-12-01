from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import default
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):            
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)		
		
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
	
    def __unicode__(self):           
		return self.choice_text
 	
# 	def __unicode__(self):		   
# 		return self.choice_text
 	
class Groups(models.Model):
	group_name = models.CharField(max_length=200)
	group_link = models.CharField(max_length=200, default='default')
	user_own = models.ForeignKey(User , related_name='Groups_user_own')
	is_important = models.IntegerField(default=0)
	keyword = models.CharField(max_length=200)
# 	
# 	def __unicode__(self):		   
# 		return self.choice_text

class Posts(models.Model):
	user_who_post = models.ForeignKey(User)
	group_that_was_post = models.ForeignKey(Groups)
	keyword = models.CharField(max_length=200)
	post_text = models.TextField()
	link =  models.CharField(max_length=500)
	pub_date = models.IntegerField()
	
class Scans(models.Model):
	time_of_the_scan = models.IntegerField()