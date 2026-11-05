age = int(input("What is your age? "))

if age >= 0:
    if age < 10:
        print("You are too young to enroll in this class.")
    elif age < 21:
        print("You can enroll in this class.")
    else:
        print("You are too old to enroll in this class.")
else:
    print("You have not input a valid number.")