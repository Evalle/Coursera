import re
try:
    fhandler = open("actual_data.txt")
except FileNotFoundError:
    fhandler = open(input("Your filename: "))
lst = list()
# s = summ
s = 0
for line in fhandler:
    result = re.findall('[0-9]+', line)
    for i in result:
        if len(i) != 0:
            lst.append(i)
for i in lst:
    s += int(i)
print(s)
