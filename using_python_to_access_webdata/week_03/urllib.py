import urllib
fhand = urllib.open('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print((line.strip()))