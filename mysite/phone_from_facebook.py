# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from polls.models import Choice, Question , Users , Groups ,posts
import unittest, time, re
import urllib2
        
import re

class facebook_phone:

    def __init__(self , email , password):
        self.user_details = {"email": email , "password": password}
        self.home_url = "https://www.facebook.com"
        self.group_pattern_url = "https://www.facebook.com/groups/"
        self.all_my_group_url = "https://www.facebook.com/groups/?category=membership"
        
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver = webdriver.Chrome()
    
    
    def start_surfing(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.home_url)
        
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(self.user_details["email"])
        self.driver.find_element_by_id("pass").clear()
        self.driver.find_element_by_id("pass").send_keys(self.user_details["password"])
        self.driver.find_element_by_id("loginbutton").click()  
    
    
    
    def get_all_group_of_user(self):
        self.start_surfing()
        self.list_of_all_groups = self.collect_groups()
        return self.list_of_all_groups

    def get_the_relevant_posts(self ,list_of_groups ):
        self.start_surfing()
        relevant_post = self.collect_data(list_of_groups)
#         return self.list_of_all_groups            

            
    def collect_groups(self):
        groups_data = []
        group_pattern_for_groups_links = 'href="/groups/(.+?)"'
        pattern_for_extracting_all_groups_names = '/ajax/hovercard/group\.php\?id=[0-9]*">(.+?)</a>'
        
        self.driver.get(self.all_my_group_url)
        groups_html = self.driver.page_source.encode('utf-8')
        
        list_of_groups_links = re.findall(group_pattern_for_groups_links, groups_html)
        fixed_list_of_groups_links = self.fix_groups_links(list_of_groups_links)
        list_of_groups_names = re.findall(pattern_for_extracting_all_groups_names, groups_html)
        
        for i in range(len(list_of_groups_names)):
            group_data_elemnt = {"name":list_of_groups_names[i], "link":fixed_list_of_groups_links[i] }
            groups_data.append(group_data_elemnt)
            
        return groups_data

    def collect_data(self , list_of_groups):
        pattern = '<p>(.+?)</p>'
        for group in list_of_groups:
            print group.group_link

        group_name_pattern = 'id="pageTitle">(.+?)</title>'
        fo = open("htmlGroupFile3.txt", "w+")
        for group in list_of_groups:
                self.driver.get(self.group_pattern_url + group.group_link)
                page_html = self.driver.page_source.encode('utf-8') 
                group_name = self.get_data_from_pattern(group_name_pattern, page_html)
                print "we now in group: "  + group_name
                fo.write("we now in group: "  + group_name+'\n')
    #             self.join_group(page_html)
                query_appearences = self.driver.find_elements_by_name("query")
                if len(query_appearences)>1:
                    search_box = query_appearences[1]
                    search_box.clear()
                    search_box.send_keys(group.keyword)
                    self.driver.find_element_by_xpath('//button[@type="submit" and @title="Search this group"]').click()
                    html = self.driver.page_source.encode('utf-8') 
                    all_results = re.findall(pattern, html)
                    for result in all_results:
                        new_post = posts(user_id = group.user_own_id, group_id = group.id , keyword = group.keyword ,post_text = result ,link = "aaaa"  )
                        new_post.save()

        fo.close()  

    def fix_groups_links(self,list_of_groups_links):
        fixed_list_of_groups_links = []
        for group_link in list_of_groups_links:
            if not (group_link == "?category=top" or group_link == "?category=friends" or group_link == "?category=local" or not group_link.endswith('/')):
                fixed_list_of_groups_links.append(group_link)  
        return fixed_list_of_groups_links
              
    def join_group(self,html_page):
        if "Join Group" in html_page:
            self.driver.find_element_by_link_text("Join Group").click()
            
    def get_data_from_pattern(self,pattern , text):           
        name = re.search(pattern, text)
        if name:
            found = name.group(1)
            return found

