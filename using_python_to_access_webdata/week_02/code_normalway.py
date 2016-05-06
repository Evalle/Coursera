try:
    fhand = open("actual_da.txt")
except FileNotFoundError:
    fhand = open(input("Your filename: "))
lst = list()
sum = 0
for line in fhand:
    words = line.split()
    for i in words:
        if i.isdigit():
            sum += int(i)
print(sum)


