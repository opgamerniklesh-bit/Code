medical_cause = input("Do you have a medical cause for your condition? (Y/N): ")

if medical_cause == "Y":
    print("You are allowed to take the test.")
else:
    attend = float(input("What is your attendance percentage? "))
    if attend >= 75:
        print("You are allowed to take the test.")
    else:
        print("You are not allowed to take the test.")