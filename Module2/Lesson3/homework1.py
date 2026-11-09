dig = int(input("Enter a number: "))
temp = 0
tempdig = dig

while dig > 0:
        temp += 1
        dig = dig // 10

print(f"The number of the digits in {tempdig}: {temp}")