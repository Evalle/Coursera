from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) # for counting inside of the list
lst = list()

for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        lst.append(tag)
    url = lst[position-1].get('href', None)
    del lst[:]
print('Retrieving: ', url)





        #for tag in tags:
#    print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)

#tag.get('href', )