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