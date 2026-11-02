char = input("Please enter a character(as in number or letter): ")
char = char.lower()
if char.isalpha():
    print("You entered a letter in the alphabet")
else:
    print("You entered a number")