hours = float(input("hours: "))
rate = float(input("rate: "))
if hours > 40 :
    pay = hours * rate + (hours - 40) * rate * .5
else:
    pay = hours * rate
print("")
print("pay: ", pay)