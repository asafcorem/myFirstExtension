from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
 
from .models import Choice, Question , Users , Groups
from myFirstExtension import phone_from_facebook
import threading
from lib2to3.fixer_util import is_import
import time
from polls.models import posts


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
 
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
 
 
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
 
 
class ResultsView(generic.DetailView):
    model = Users
    template_name = 'polls/results.html'
 
def vote(request, question_id):
#     Users.objects.all().delete()
#     Groups.objects.all().delete()
    p = get_object_or_404(Question, pk=question_id)
    try:
        email =  request.POST['email']
        password =  request.POST['password']
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
        new_user = Users(user_mail=email, user_password=password)
        new_user.save()
         
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        FB_phone =  phone_from_facebook.facebook_phone(email , password)
        list_of_all_groups = FB_phone.get_all_group_of_user()
        for group in list_of_all_groups: 
            new_group = Groups(group_name = group["name"] ,group_link = group["link"], user_own = new_user)
            new_group.save()
        return HttpResponseRedirect(reverse('polls:results', args=(new_user.id,)))
     
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
    return HttpResponseRedirect(reverse('polls:results', args=(user_id,)))    

def scan_thread():
    while(True):
        all_users =  Users.objects.all()
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
    posts.objects.all().delete()
    t = threading.Thread(target=scan_thread)
    t.start()

    return HttpResponse("Here's the text of the Web page.") 

def look_for_new_posts(user_details):
    relevant_groups = Groups.objects.filter(user_own_id = user_details.id , is_important = "1")
    FB_phone =  phone_from_facebook.facebook_phone(user_details.user_mail , user_details.user_password)
    FB_phone.get_the_relevant_posts(relevant_groups)

