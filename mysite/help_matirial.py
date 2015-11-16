         

# >>> Question.objects.all()
# [<Question: What's up?>]
# >>> Question.objects.filter(id=1)
# [<Question: What's up?>]
# >>> Question.objects.filter(question_text__startswith='What')
# [<Question: What's up?>]
# >>> from django.utils import timezone
# >>> current_year = timezone.now().year
# >>> Question.objects.get(pub_date__year=current_year)
# <Question: What's up?>
# >>> Question.objects.get(id=2)
# Traceback (most recent call last):
#     ...
# DoesNotExist: Question matching query does not exist.
# >>> Question.objects.get(pk=1)
# <Question: What's up?>
# >>> q = Question.objects.get(pk=1)
# >>> q.was_published_recently()
# True
# >>> q = Question.objects.get(pk=1)
# >>> q.choice_set.all()
# []
# >>> q.choice_set.create(choice_text='Not much', votes=0)



#     prepare()


# def prepare():      
#         //*[@id="u_0_5"]/a
#         <a class="mrm _42ft _4jy0 _4jy4 _517h _51sy" role="button" href="#" 
#         ajaxify="/ajax/groups/membership/r2j.php?ref=group_jump_header&amp;group_id=359442890872128" 
#         rel="async-post">Join Group</a>
        
        
                
#     while 1:
#             print 555
#             print driver.find_element_by_css_selector("a.mainNav.mainNavWidthOne > img")
#             print driver.find_element_by_css_selector("a.mainNav.mainNavWidthOne > img").click()
#             print 97923874
#             counter = 1
#             
#             while driver.find_elements_by_class_name("medblue10")[counter].tag_name == 'span':
#                 print counter
#                 counter = counter + 3
#             print 38273354
#             driver.find_elements_by_class_name("medblue10")[counter].click()
#             print 382374
#             #return 1
#            # print driver.page_source
#             html_page = driver.page_source
#             found = re.search('medblue14(.+?)</a>', html_page)
#             print found
#             found = found.group(1)
#             print found
#             theName = re.search('>(.*)', found)
#             print theName
#             theName = theName.group(1)   
#             sentence = theName
#             result = -1
#             rev_sentence = ""
#             for i in range(len(sentence.split()),0,-1):
#                 rev_sentence += sentence.split()[i-1] + " " 
# 
#             print 57867
#             print result
#             foundTitle = re.search('h1(.+?)</h1>', html_page)
#             print foundTitle
#             foundTitle = foundTitle.group(1)
#             print foundTitle
#             projectName = re.search('>(.*)', foundTitle)
#             print projectName
#             projectName = projectName.group(1)  
#             sentence = projectName
#             rev_sentence = ""
#             for i in range(len(sentence.split()),0,-1):
#                 rev_sentence += sentence.split()[i-1] + " " 
#             
#             some_input = easygui.indexbox(msg=rev_sentence, title=' ', choices=('regular-man', 'regular woman' , 'regular plural' , 'kidum man', 'kidum woman',' kidum plural ' ,'regular + kidum man', 'regular + kidum woman' , 'regular +kidum plural','stop','delete'), image=None)
#             if some_input == 0:
#                 print 63463
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\mans', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
#                 print 834671
#             elif some_input == 1:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\womans', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
#             elif some_input == 2:
#                 print 8754970
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\plural', 'r')
#                 print 24232
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
#             elif some_input == 3:
#                 print 34564356
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\kidum', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutKidum.pdf"
#                 print 5465
#             elif some_input == 4:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\kidumWoman', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutKidum.pdf"
#             elif some_input == 5:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\kidumPlural', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutKidum.pdf"
#             elif some_input == 6:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\reg+kidum_man', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
#             elif some_input == 7:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\reg+kidum_woman', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
#             elif some_input == 8:
#                 f = open('C:\\Users\\Toshiba\\Desktop\\workspace\\xplace\\main\\reg+kidum_plural', 'r')
#                 about = "C:\\Users\\Toshiba\\Desktop\\aboutUs.pdf"
# 
#             elif some_input == 10:
#                 print 77777
#                 #print html_page
#                 foundTitle = re.search('bids.projectId = (.+?);', html_page)
#                 print 77777
#                 print foundTitle
#                 print 77777
#                 foundTitle = foundTitle.group(1)
#                 print 'p'+foundTitle+'j'
#                 deleteString = "#"+foundTitle+" > td > input[name=\"p\"]"
#                 print deleteString
#                 driver.find_element_by_css_selector("a.mainNav.mainNavWidthOne > img").click()
#                 driver.find_element_by_name("p").click()
#                 driver.find_element_by_id("removeRecommendationButton").click()
#                 continue
# 
#            
#             driver.find_element_by_id("chEscrow").click()
#             driver.find_element_by_id("bidComment").click()
#             driver.find_element_by_id("bidComment").clear()     
#             driver.find_element_by_id("bidTypeHour").click()
#             print 22
#             driver.find_element_by_id("bid1").click()
#             driver.find_element_by_id("bid1").clear()
#             driver.find_element_by_id("bid1").send_keys("200")
#                                                                                                                    
#             theOffer = f.read().decode("utf-8")
#             driver.find_element_by_id("bidComment").send_keys(u"הי " + result + " :)")
#             print 9364894
#             driver.find_element_by_id("bidComment").send_keys(theOffer)
#             print 12243245
#             driver.find_element_by_id("anonymous").click()
#             driver.find_element_by_link_text(u"פרטים נוספים »").click()
#             driver.find_element_by_name("file1").send_keys(about)
#             driver.find_element_by_name("submitButton").click()
#             driver.find_elements_by_name("_finish")[1].click()
#             # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
#             driver.find_element_by_css_selector("a.mainNav.mainNavWidthOne > img").click()
#             driver.find_element_by_link_text(u"העבר לארכיון").click()
#         
#     def is_element_present(self, how, what):
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException, e: return False
#         return True
#     
#     def is_alert_present(self):
#         self.driver.switch_to_alert()
#         return True
#     
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
#     
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
