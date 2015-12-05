'''
Created on Nov 20, 2015

@author: asaf
'''
import re

class utils:
    patterns_dic = {'home_url': 'https://www.facebook.com' , "group_pattern_url":"https://www.facebook.com/groups/" , 
                    "all_my_group_url":"https://www.facebook.com/groups/?category=membership" , "group_pattern_for_groups_links": 'href="/groups/(.+?)"',
                    "pattern_for_extracting_all_groups_names":'/ajax/hovercard/group\.php\?id=[0-9]*">(.+?)</a>' , 
                    "result_pattern":'<p>(.+?)</p>' , "link_pattern":'/permalink/(.+?)/' , "epoch_time_pattern":'data-utime=\"(.+?)\"',
                    "group_name_pattern" : 'id="pageTitle">(.+?)</title>'}
            
    def __init__(self, params):
        a=1
        
        
def fix_groups_links(list_of_groups_links):
    print "before cleaning"
    fixed_list_of_groups_links = []
    for group_link in list_of_groups_links:
        print group_link
        if not (group_link == "?category=top" or group_link == "?category=friends" or group_link == "?category=local" or not group_link.endswith('/') or 
                group_link.endswith('pending/') or group_link.endswith('requests/')):
            fixed_list_of_groups_links.append(group_link)  
    return fixed_list_of_groups_links
          
def get_data_from_pattern(pattern , text):           
    name = re.search(pattern, text)
    if name:
        found = name.group(1)
        return found        