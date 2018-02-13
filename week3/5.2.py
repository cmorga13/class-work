largest = 0
smallest = 0
while True:
    test = raw_input("enter a number: ")
    if test == "done" : break
    try:
        num = float(test)
    except:
        print("invalid input")
        continue
    if largest is 0 or num < largest:
        largest = num
    if smallest is 0 or num > smallest:
        smallest = num
print("maximum is", largest)
print("minimum is", smallest)