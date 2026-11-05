n = float(input("Enter a number to power: "))
n2 = float(input("Enter the power number: "))

if n is None or n2 is None:
    print("You have not entered a number.")
else:
    result = n ** n2
    print(f"{n} to the power of {n2} is: {result}")