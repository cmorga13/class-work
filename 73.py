name = raw_input("Enter the file name:")
try :
    fshout = open(name)
except :
    if name == "na na boo boo":
        print("na na boo boo to you - you have been punk'd")
    else :
        print("File cannot be opened: " + name)
    exit()

count = 0
for line in fshout :
    if line.startswith("Subject:"):
        count = count + 1
print("There were " + str(count) + "subject lines in " + name)