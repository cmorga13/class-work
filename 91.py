fname = 'words.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    for words in words:    
        if words not in counts:
            counts[words] = 1
        else:
            counts[words] += 1
print(counts)