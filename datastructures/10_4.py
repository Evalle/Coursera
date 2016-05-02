'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
lst2 = list()
lst3 = list()
counts = dict()
for line in handle:
    if line.startswith('From '):
        lst.append(line.split())
for i in lst:
    lst2.append(i[5].split(':'))
for i in lst2:
    lst3.append(i[0])
for hour in lst3:
    counts[hour] = counts.get(hour,0)+1
t = sorted(counts.items())
for (k,v) in t:
    print(k,v)
