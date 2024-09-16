import os
import subprocess
import json

from utils import *

rules_json = get_rules()

open_akiflow()

app = get_frontmost_app()

if app == rules_json["default_browser"]:
    url = get_url(app)
    
for rule in rules_json["rules"]:
    try:
        if app == rule.get("frontmost_app", ""):
            if "tags" in rule.keys():
                for tag in rule["tags"]:
                    input_tag(tag)
            if "project" in rule.keys():
                input_project(rule["project"])
            break

        elif rule["url"] in url:
            if "tags" in rule.keys():
                for tag in rule["tags"]:
                    input_tag(tag)
            if "project" in rule.keys():
                input_project(rule["project"])
            break
    except:
        pass



# def process_url(url):
#     attributes = {
#         'tags' : [],
#     }

#     if '1497427' in url or 'adrianapicoral' in url:
#         attributes['project'] = 'university'
#         attributes['tags'].append('210')
#     elif '1487819' in url:
#         attributes['project'] = 'university'
#         attributes['tags'].append('244')
#     elif '1472921' in url or 'mastering' in url:
#         attributes['project'] = 'university'
#         attributes['tags'].append('141')
#     elif '1483088' in url:
#         attributes['project'] = 'university'
#         attributes['tags'].append('150C1')
#     elif 'handshake' in url or 'linkedin' in url:
#         attributes['project'] = 'personal'
#         attributes['tags'].append('professional')

#     return attributes

# app = get_frontmost_app()

# attributes = None

# if app == 'Arc':
#     url = subprocess.check_output(['osascript', '-e', 'tell application "Arc" to get URL of active tab of window 1'], universal_newlines=True).strip()
#     attributes = process_url(url)
# elif app == 'Superhuman':
#     cmd = """
#         tell application "System Events"
#             tell process "Superhuman"
#                 get value of static text 1 of group 2 of group 1 of group 1 of group 1 of group 1 of UI element 1 of group 1 of group 1 of group 1 of group 1 of window 1
#             end tell
#         end tell"""
#     inbox = subprocess.check_output(['osascript', '-e', cmd], universal_newlines=True).strip()
#     if 'andyjsiegel1@gmail.com' in inbox:
#         project = 'personal'
#     elif 'siegela1@arizona.edu' in inbox:
#         project = 'university'
#     attributes = { 'tags' : ['Email'], 'project' : project }

# open_akiflow()

# if attributes is not None:
#     for tag in attributes['tags']:
#         input_tag(tag)

#     if 'project' in attributes:
#         input_project(attributes['project'])