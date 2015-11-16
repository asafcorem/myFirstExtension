from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import default

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
	
class Users(models.Model):
	user_mail = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)
 	
# 	def __unicode__(self):		   
# 		return self.choice_text
 	
class Groups(models.Model):
	group_name = models.CharField(max_length=200)
	group_link = models.CharField(max_length=200, default='default')
	user_own = models.ForeignKey(Users)
	is_important = models.IntegerField(default=0)
	keyword = models.CharField(max_length=200)
# 	
# 	def __unicode__(self):		   
# 		return self.choice_text


class posts(models.Model):
	user_id = models.IntegerField(default=0)
	group_id = models.IntegerField(default=0)
	keyword = models.CharField(max_length=200)
	post_text = models.TextField()
	link =  models.CharField(max_length=500)
	pub_date = models.DateTimeField(default = datetime.datetime.now())