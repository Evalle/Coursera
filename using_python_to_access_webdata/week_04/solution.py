from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter: ')

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

for tag in tags:
   sum += (int(tag.contents[0]))
