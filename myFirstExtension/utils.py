'''
Created on Nov 20, 2015

@author: asaf
'''

class utils:
    patterns_dic = {'home_url': 'https://www.facebook.com' , "group_pattern_url":"https://www.facebook.com/groups/" , 
                    "all_my_group_url":"https://www.facebook.com/groups/?category=membership" , "group_pattern_for_groups_links": 'href="/groups/(.+?)"',
                    "pattern_for_extracting_all_groups_names":'/ajax/hovercard/group\.php\?id=[0-9]*">(.+?)</a>' , 
                    "result_pattern":'<p>(.+?)</p>' , "link_pattern":'/permalink/(.+?)/' , "epoch_time_pattern":'data-utime=\"(.+?)\"',
                    "group_name_pattern" : 'id="pageTitle">(.+?)</title>'}
            


    def __init__(self, params):
        a=1
        