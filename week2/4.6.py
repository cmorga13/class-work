def computepay(hours, rate):   
    if hours > 40 :
        pay = hours * rate + (hours - 40) * rate * .5
    else:
        pay = hours * rate
    return pay
try:
    hours = float(input("hours: "))
    rate = float(input("rate: "))
except:
    print("")
    print("entries must be numbers")
    quit()
     
total = computepay (hours, rate)
print("")
print("pay: ", total)