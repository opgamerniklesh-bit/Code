a = 20
b = 15
c = 20

print (not(a == b))
print (not(b == c))

a = str("Hello")
b = str("World")

if (not(a == b)):
    print("a and b are not equal")

a = 1
b = 15

if not((a == 1) or (b == 5)):
    print("Hello")
else:
    print ("a is not equal to 1 or b is not equal to 5")

a = int(input("Enter a number: "))
if a % 2 != 0:
    print("The number is not even")
else:
    print("The number is even")