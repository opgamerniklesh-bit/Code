age = int(input("Enter your age: "))
if age > 10:
    print ("You are too young to join the class.")
    if age >= 10:
        print ("You are eligible to join the class.")
        if age > 20:
            print ("You are too old to join the class.")
else:
    print ("You have not input a number")