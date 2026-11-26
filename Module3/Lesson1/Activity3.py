def add (p, q):
    return p + q

def sub (p, q):
    return p - q

def multi (p, q):
    return p * q

def divi (p, q):
    return p / q

print ("There are 4 choices of calculation\n a) Add\n b) Subtract\n c) Multiply\n d) Divide")
choice = input("Which calculation do you choise?")
num1 = float(input("Enter your first number"))
num2 = float(input("Enter your second number"))

if choice == "a":
    reslut = add (num1, num2)
    print (reslut)
elif choice == "b":
    reslut = sub (num1, num2)
    print (reslut)
elif choice == "c":
    reslut = multi (num1, num2)
    print (reslut)
elif choice == "d":
    reslut = divi (num1, num2)
    print (reslut)
else:
    print ("Invalid letter or number")