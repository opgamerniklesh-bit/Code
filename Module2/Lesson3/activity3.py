num = int(input("Enter a number to check if it is an Armstrong number: "))
sum = 0
temp = num
numofnum = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** numofnum
    temp = temp // 10

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")