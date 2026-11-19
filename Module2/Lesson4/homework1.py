num = float(input("Enter a positive decimal number: "))
tnum = num

if num == 0:
    binary = "0"
else:
    binary = ""
    while num > 0:
        rem = int(num % 2)
        binary = str(rem) + binary
        num = int(num / 2)

print(f"The binary representation of {tnum} is {binary}")