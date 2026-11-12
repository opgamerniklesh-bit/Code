num = int(input("Enter a number: "))
t = num
numlen = 0

while t > 0:
    numlen += 1
    t = int(t / 10)

if numlen >= 4:
    numlen = int(numlen / 2)
    chk = 0
    while num > 0:
        rem = num % 10
        if chk == numlen:
            midtwo = rem
        elif chk == (numlen - 1):
            midone = rem
        num = int(num / 10)
        chk += 1
    prod = midone * midtwo
    print("The product of the middle two digits is:", prod)
else:
    print ("It is not a four digit number")