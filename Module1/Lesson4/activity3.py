math = input("Enter your math score: ")
english = input("Enter your English score: ")
science = input("Enter your science score: ")
hindi = input("Enter your Hindi score: ")

sum = int(math) + int(english) + int(science) + int(hindi)
print("Your total score is: ", sum)

perc = sum / 400 * 100
print("Your percentage is: ", perc)