import re
try:
    fhand = open('_data.txt')
except FileNotFoundError:
    fhand = open(input('Your filename: '))
lst = list()
for line in fhand:
    y = re.findall('[0-9]+', line)
    if len(y) != 0:
        lst.append(y)
lst = (sum(lst, []))
sum = 0
for i in lst:
    sum+=int(i)
print(sum)




