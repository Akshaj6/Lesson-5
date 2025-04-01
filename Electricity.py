units = int(input("How many units did you use? "))
if units<50:
    print("Your bill is ", (units*2.60)+25)
elif units<=100:
    print("Your bill is ", (units*3.25)+35)
elif units<=200:
    print("Your bill is ", (units*5.26)+45)
elif units>200:
    print("Your bill is ", (units*8.45)+75)