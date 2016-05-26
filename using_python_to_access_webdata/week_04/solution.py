from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
#count = int(input('Enter count: '))
position = int(input('Enter position: '))

def followtheleader(url, position):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    lst = list()

    for link in soup.find_all('a'):
        lst.append((link.get('href')))

    return(lst[position-1])

print(followtheleader(url, position))

#for tag in tags:
#    print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)

#tag.get('href', )