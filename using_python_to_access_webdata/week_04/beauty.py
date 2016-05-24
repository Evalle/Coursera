from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = input('Enter - ')
html = urlopen('http://python-data.dr-chuck.net/comments_42.html')
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

for tag in tags:
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)