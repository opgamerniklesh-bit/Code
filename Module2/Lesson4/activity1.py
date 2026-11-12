string = str(input("Enter a word: "))
char = str(input("Enter a character: "))
i = 0
count = 0

while i < len(string):
    if string[i] == char:
        count += 1
    i += 1

print (f"The character '{char}' appears {count} times in the word '{string}'.")