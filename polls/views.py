from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.models import User
 
from .models import Choice, Question ,Groups
from myFirstExtension import phone_from_facebook
import threading
from lib2to3.fixer_util import is_import
import time
from polls.models import Posts,Scans
from datetime import date
import calendar
from django.shortcuts import redirect
import bz2


class IndexView(generic.DetailView):
    model = User
    template_name = 'polls/index.html'
 
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_object(self):
        new_user , created = User.objects.get_or_create(username="sadsadasd", password="asds")
        return get_object_or_404(User, pk=new_user.id)
 
 
class ResultsView(generic.DetailView):
    model = User
    template_name = 'polls/results.html'
 
def vote(request,asdsad):
    user_email =  request.POST['email']
    user_password =  request.POST['password'].encode('utf-8')
    
    FB_phone =  phone_from_facebook.facebook_phone(user_email , user_password)
    list_of_all_groups = FB_phone.get_all_group_of_user()
    user = User.objects.create_user(password = user_password , username = user_email ,first_name = user_password)
    if len(list_of_all_groups)>0:           
        user.save()
        for group in list_of_all_groups: 
            new_group = Groups(group_name = group["name"] ,group_link = group["link"], user_own = user)
            new_group.save()  
                       
    return HttpResponseRedirect(reverse('polls:results', args=(user.id,)))
     
def saving(request, user_id):
    all_checked_groups = request.POST.getlist("group_to_mark")
    keyword = request.POST['keyword'] 
    for a in all_checked_groups:
        print "group id is"
        print a
        p = get_object_or_404(Groups, pk=a)
        p.is_important=1
        p.keyword = keyword
        p.save()
    first_scan_for_user(user_id)
    a = User.objects.get(id = user_id)
    print a
    print a.id
    return HttpResponseRedirect(reverse('polls:posts_display', args=(a.id,)))  

def scan_thread():
    while(True):
        all_users =  User.objects.all()
        print all_users
        print len(all_users)
        threads = []
        i = 0
        for user_details in all_users:
            if i==0:
                t = threading.Thread(target=look_for_new_posts(user_details))
                threads.append(t)
                t.start()
            i = i + 1
        
        print 'Worker'
        time.sleep(600000)

def start_scan(request, question_id):
    epoch_time = int(time.time())
    new_scan = Scans(time_of_the_scan = epoch_time)
    new_scan.save()
    Posts.objects.all().delete()
    t = threading.Thread(target=scan_thread)
    t.start()
    return HttpResponse("Here's the text of the Web page.") 

def first_scan_for_user(user_id):
    epoch_time = int(time.time())
    new_scan = Scans(time_of_the_scan = epoch_time)
    new_scan.save()
    look_for_new_posts(user_id)
    print "aaaaaaaaaaadasdsfd"

  
def look_for_new_posts(user_id):
    user = User.objects.get(id = user_id)
#     user_details = {"user_mail":user.email , "user_password":user.password}
    relevant_groups = Groups.objects.filter(user_own =user , is_important = "1")
    FB_phone =  phone_from_facebook.facebook_phone(user.username ,user.first_name )
    FB_phone.get_the_relevant_posts(relevant_groups)
    
def clean_data_bases(request):
    print "1111111"
    User.objects.all().delete()
    Groups.objects.all().delete()
    Posts.objects.all().delete()
    return HttpResponse("we cleaned all") 
