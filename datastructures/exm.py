counts = dict()
text = open('text.txt', 'r')
lines = text.read().split( )
for word in lines:
    counts[word] = counts.get(word, 0) + 1
print counts
