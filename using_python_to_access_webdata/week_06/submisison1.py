import json
import urllib.request

request = 'http://python-data.dr-chuck.net/comments_244512.json'

uh = urllib.request.urlopen(request)
data = uh.read()

info = json.loads(data.decode('utf-8'))

sum = 0

for i in info["comments"]:
    sum += (i["count"])
print(sum)