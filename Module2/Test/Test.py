sec = 12
lives = 5

while lives > 0:
    plynum = int(input("Enter a number from 1 to 50 to get a secret number!"))
    if plynum == 12:
        print ("You WIN!!!")
        break
    elif plynum == 11 or 13:
        print ("Hot")
    elif plynum in range(7,10) or range(14,17):
        print ("Warm")
    elif plynum in range(3,6) or range(18,15):
        print ("Cold")
    elif plynum in range(1,2) or range(16,50):
        print ("Ice cold")
    else:
        lives = lives - 1
        print ("Try again")
        print ("You have",lives,"left")

if lives == 0:
    print ("The secret number was", sec)