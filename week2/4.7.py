try:
    entry = float(input("Enter 0.0 to 1: "))
    if entry >= 0.0 and entry <= 1:
        pass
    else:
        print("wrong")
    quit()

except:
def computegrade(score):
    if score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    else:
        print("F")
        quit()