from urllib.request import urlopen

fhand = urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.strip().decode('utf-8'))