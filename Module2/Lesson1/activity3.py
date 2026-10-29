choice1 = input ("What ride do you select?\n"
                "1 - Bike\n"
                "2 - Car\n")

if choice1 == "1":
    choice2 =  input ("What type of bike?\n"
                      "1 - scooter:\n"
                      "2 - scooty:")
    if choice2 == "1":
        print ("You have selected a scooter")
    else:
        print ("You have selected a scooty")
elif choice1 == "2":
    choice3 =  input ("What type of car?\n"
                      "1 - XUV:\n"
                      "2 - Sedan:")
    if choice3 == "1":
        print ("You have selected a XUV")
    else:
        print ("You have selected a Sedan")
else:
    print ("Invalid choice")