# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options


from polls.models import Choice, Question , Groups ,Posts
from myFirstExtension import utils
import unittest, time, re
import urllib2
        
import re

class facebook_phone:

    def __init__(self , email , password):
        
        self.patterns = utils.utils.patterns_dic
        self.user_details = {"email": email , "password": password}        
        self.verificationErrors = []
        self.accept_next_alert = True
        
        
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.notifications":2}
        chromeOptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
          
    
#         self.driver = webdriver.Chrome()
    
    def start_surfing(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.patterns["home_url"])
        
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(self.user_details["email"])
        self.driver.find_element_by_id("pass").clear()
        self.driver.find_element_by_id("pass").send_keys(self.user_details["password"])
        self.driver.find_element_by_id("loginbutton").click()  
    
    def get_all_group_of_user(self):
        self.start_surfing()
        self.list_of_all_groups = self.collect_groups()
        self.driver.close()
        return self.list_of_all_groups

    def get_the_relevant_posts(self ,list_of_groups ):
        self.start_surfing()
        relevant_post = self.collect_data(list_of_groups)
        self.driver.close()

    def collect_groups(self):
        groups_data = []
        self.driver.get(self.patterns["all_my_group_url"])
        groups_html = self.driver.page_source.encode('utf-8')
        
        list_of_groups_links = re.findall(self.patterns["group_pattern_for_groups_links"], groups_html)
        fixed_list_of_groups_links = utils.fix_groups_links(list_of_groups_links)
        list_of_groups_names = re.findall(self.patterns["pattern_for_extracting_all_groups_names"], groups_html)
        
        print " all the names  "
        for i in range(len(list_of_groups_names)):
            print list_of_groups_names[i]
            print fixed_list_of_groups_links[i]
            group_data_elemnt = {"name":list_of_groups_names[i], "link":fixed_list_of_groups_links[i] }
            groups_data.append(group_data_elemnt)
            
        return groups_data

    def collect_data(self , list_of_groups):
        for group in list_of_groups:
                self.driver.get(self.patterns["group_pattern_url"] + group.group_link)
                page_html = self.driver.page_source.encode('utf-8') 
                group_name = utils.get_data_from_pattern(self.patterns["group_name_pattern"], page_html)
                print "we now in group: "  + group_name
    #             self.join_group(page_html)
                query_appearences = self.driver.find_elements_by_name("query")
                if query_appearences:
                    search_box = query_appearences[1]
                    search_box.clear()
                    search_box.send_keys(group.keyword)
                    self.driver.find_element_by_xpath('//button[@type="submit" and @title="Search this group"]').click()
                    html = self.driver.page_source.encode('utf-8') 
                    post_data = self.get_posts_with_links_and_time(html)
                    if len(post_data["link"]) > 0:
                        for i in range(len(post_data["link"])):
                            if not post_data["link"][i] == None:
                                new_post = Posts(user_who_post_id = group.user_own_id, group_that_was_post_id = group.id , keyword = group.keyword ,post_text = post_data["results"][i] ,link = post_data["link"][i]  , pub_date =post_data["all_epoch_time"][i] )
                                new_post.save()        
        
    def join_group(self,html_page):
        if "Join Group" in html_page:
            self.driver.find_element_by_link_text("Join Group").click()
        
    def get_posts_with_links_and_time(self,html):
        post_data = {}
        post_data["link"] = []
        post_data["results"] = []
        post_data["all_epoch_time"] = []
        
        posts_division = html.split("userContentWrapper _5pcr")
        del posts_division[0]
        for post in posts_division:
            post_data["link"].append(utils.get_data_from_pattern(self.patterns["link_pattern"], post))
            post_data["results"].append(''.join(re.findall(self.patterns["result_pattern"], post)))
            post_data["all_epoch_time"].append(utils.get_data_from_pattern(self.patterns["epoch_time_pattern"], post))
        
        return post_data
