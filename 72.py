name = raw_input("Enter a file name: ")
fshout = open(name)
count = 0
total = 0
for line in fshout :
    if line.startswith("X-DSPAM-Confidence:") :
        vline = float(line[20:])
        total = total + vline
        count = count + 1
print("Average spam confidence", total, count)