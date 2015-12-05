import bz2
import calendar
from datetime import date
from lib2to3.fixer_util import is_import
import threading
import time

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import DetailView

from myFirstExtension import phone_from_facebook
from polls.models import Posts, Scans

from .models import Choice, Question , Groups


class IndexView(generic.DetailView):
    template_name = 'polls/index.html'
    def get_object(self):
        user_by_the_url = get_object_or_404(User, pk=self.kwargs['pk'])
        user_by_session =  self.request.user
        if user_by_the_url == user_by_session:
            return user_by_the_url
        else:
            return get_object_or_404(User, pk="1111") 
        
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['last_scan'] = Scans.objects.order_by('-id')[0]
        return context        
        
    
class DetailView(generic.DetailView):
    def get_object(self):
        IndexView()
        if self.request.user.is_authenticated():
            return self.request.user
        else:    
            return None
 
    def get_template_names(self):
        if self.request.user.is_authenticated():
            return 'polls/index.html'
        else:    
            return 'polls/detail.html'
        
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.request.user.is_authenticated():
            context['last_scan'] = Scans.objects.order_by('-id')[0]
        return context    
 
class ResultsView(generic.DetailView):
    model = User
    template_name = 'polls/results.html'
 
def vote(request,asdsad):
    user_email =  request.POST['email']
    user_password =  request.POST['password']
    
    user = authenticate(username=user_email, password=user_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('polls:posts_display', args=(user.id,)))  
    else:
        if new_user_register(user_email , user_password):
            new_user = authenticate(username=user_email, password=user_password)
            login(request, new_user)
            return HttpResponseRedirect(reverse('polls:results', args=(new_user.id,)))
        else:
            return HttpResponse("there is no group to show - maybe the password or name was not correct , and maybe you dont have any groups") 

     
def saving(request, user_id):
    all_checked_groups = request.POST.getlist("group_to_mark")
    keyword = request.POST['keyword'] 
    for a in all_checked_groups:
        p = get_object_or_404(Groups, pk=a)
        p.is_important=1
        p.keyword = keyword
        p.save()
    first_scan_for_user(user_id)
    user = User.objects.get(id = user_id)
    return HttpResponseRedirect(reverse('polls:posts_display', args=(user.id,)))  

def scan_thread():
    while(True):
        print "start check"
        all_users =  User.objects.all()
        for user in all_users:
                look_for_new_posts(user.id)
        print 'Worker'
        time.sleep(60)

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

  
def look_for_new_posts(user_id):
    user = User.objects.get(id = user_id)
#     user_details = {"user_mail":user.email , "user_password":user.password}
    relevant_groups = Groups.objects.filter(user_own =user , is_important = "1")
    FB_phone =  phone_from_facebook.facebook_phone(user.username ,user.first_name )
    FB_phone.get_the_relevant_posts(relevant_groups)
    
def clean_data_bases(request):
    User.objects.all().delete()
    Groups.objects.all().delete()
    Posts.objects.all().delete()
    return HttpResponse("we cleaned all") 

def clean_one_user_data(request):
    print "lalala"
    user_name =  request.POST['username']
    print user_name
    user = User.objects.get(username = user_name)
    Posts.objects.filter(user_who_post_id = user.id).delete()
    Groups.objects.filter(user_own_id = user.id).delete()
    user.delete()
    return HttpResponse("we cleaned one user") 

def new_user_register(user_email , user_password):
        FB_phone =  phone_from_facebook.facebook_phone(user_email , user_password)
        list_of_all_groups = FB_phone.get_all_group_of_user()
        if len(list_of_all_groups)>0:
            user = User.objects.create_user(password = user_password , username = user_email ,first_name = user_password)           
            user.save()
            print "check groups link"
            for group in list_of_all_groups: 
                print group["link"]
                new_group = Groups(group_name = group["name"] ,group_link = group["link"], user_own = user)
                new_group.save()  
            return user             
        else:
            return False
    
def log_out(request,blaasd):
    user = request.user
    logout(request)
    return HttpResponseRedirect(reverse('polls:detail', args=(user.id,)))  