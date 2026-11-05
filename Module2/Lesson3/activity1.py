n = int(input("How many numbers do you want to enter?: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
    
print(f"The sum is: {sum}")