import subprocess
import json
import os

script_dir = os.path.dirname(__file__)
rules_file = os.path.join(script_dir, 'rules.json')

def get_rules():
    with open(rules_file, 'r') as file:
        # Load the contents of the file into a Python object
        data = json.load(file)
        for index, rule in enumerate(data['rules']):
            if "frontmost_app" not in list(rule.keys()) and "url" not in list(rule.keys()):
                print(f"rule at index {index} has an error.")
                raise Exception("rules.json is invalid")
    
    return data

def get_frontmost_app():
    cmd = """
    tell application "System Events"
        set the frontmost_app to the name of the first application process whose frontmost is true
        return the frontmost_app
    end tell
    """
    try:
        frontmost_app = subprocess.check_output(['osascript', '-e', cmd], universal_newlines=True).strip()
        return frontmost_app
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def get_url(app):
    # SAFARI
    if app == "Safari":
        cmd = """
        tell application "Safari"
            set theURL to URL of current tab of window 1
        end tell
        return theURL
        """
        url = subprocess.check_output(['osascript', '-e', cmd], universal_newlines=True).strip()
        return url
    if app == "Firefox":
        raise Exception("Firefox is not supported, sorry!")
    else:
        # CHROMIUM BROWSERS
        url = subprocess.check_output(['osascript', '-e', f'tell application "{app}" to get URL of active tab of window 1'], universal_newlines=True).strip()
        return url

def open_akiflow():
    cmd = """osascript -e 'tell application "System Events" to keystroke " " using {option down}'"""
    os.system(cmd)
            
def input_tag(tag):
    cmd = f"""osascript -e 'tell application "System Events" to keystroke "*{tag}\t"'"""
    os.system(cmd)

def input_project(project):
    cmd = f"""osascript -e 'tell application "System Events" to keystroke "#{project}\t"'"""
    os.system(cmd)