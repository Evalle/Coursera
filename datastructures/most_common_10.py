#python3
fhand = open('text.txt')
count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = list()
for key,value in count.items():
    lst.append( (value,key) )

lst.sort(reverse=True)

for value,key in lst[:10]:
    print(key,value)
