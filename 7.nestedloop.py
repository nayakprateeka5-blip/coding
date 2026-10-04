grade = int(input("Enter your grade (0-100):"))
if grade >= 90:
    print("A")
else:
    if grade >= 80:
        print("B")
    else:
        if grade >= 70:
            print("C")
        else:
            print("Fail")
