n = float(input("Enter a number to power: "))
n2 = float(input("Enter the power number: "))

for i in range(1, int(n2) + 1):
    result = n ** i
    print(f"{n} to the power of {i} is: {result}")