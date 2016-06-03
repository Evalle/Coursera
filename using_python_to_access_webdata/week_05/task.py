import xml.etree.ElementTree as ET
from urllib.request import urlopen

serviceurl = "http://python-data.dr-chuck.net/comments_244508.xml"

html = urlopen(serviceurl).read()
filexml = (html).decode('utf-8')
stuff = ET.fromstring(filexml)
lst = stuff.findall('comments/comment')

lstnmbrs = list()

for item in lst:
    lstnmbrs.append(int(item.find('count').text))

sum = 0

for i in lstnmbrs:
    sum+=i

print(sum)

