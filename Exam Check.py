ques = input("Do you have a medical cause for missing school yes or no?")
attendance = int(input("Enter your attendance :"))
if ques == "yes" :
    print("You can give the exam")
else:
    if attendance >= 75 :
        print("You can give the exam")
    else:
        print("You can't give the exam")