lower = int(input("Enter a lower limit for the range: "))
upper = int(input("Enter an upper limit for the range: "))

print("The range is between", lower, "and", upper)

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            num_divisible = num % i
            if num_divisible == 0:
                break
            else:
                print(num, "is a prime number")