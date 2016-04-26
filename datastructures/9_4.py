'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
'''
name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name, 'r')
counts = dict()
for name in file:
  if name.startswith('From: '):
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
maximum = max(counts.values())
for key, value in counts.items():
    if maximum == value:
        print (key.strip('From: ')).strip('\n') + ' ' + str(value)
