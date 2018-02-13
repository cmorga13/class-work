fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print ('File not found:', fname)
    quit()
try:
    for line in fhand:
        words = line.split()
        if len(words) == 0 and words[0] == 'From' : print(words[2])
except:
    print('File:', fname, 'contains no data')
    quit()