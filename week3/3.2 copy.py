largest = 0
smallest = 0
while True:
    test = input("Enter a number: ")
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
print("Maximum is", largest)
print("Minimum is", smallest)