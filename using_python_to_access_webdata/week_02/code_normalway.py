import re
try:
    fhandler = open("actual_data.txt")
except FileNotFoundError:
    fhandler = open(input("Your filename: "))
lst = list()
# s = summ
s = 0
for line in fhandler:
    words = line.split()
    for item in words:
        if item.isdigit():
            lst.append(item)
for i in lst:
    s += int(i)
print(s)

