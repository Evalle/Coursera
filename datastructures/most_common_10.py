#python3
fhand = open('romeo.txt')
count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = list()
for key,value in counts.items():
    lst.append( (value,key) )

lst.sort(reverse=True)

for value,key in lst[:10]:
    prunt key,value
