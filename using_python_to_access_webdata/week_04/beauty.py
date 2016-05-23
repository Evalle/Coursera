from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter - ")

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for tag in tags:
    print(tag.get('href'), None)
