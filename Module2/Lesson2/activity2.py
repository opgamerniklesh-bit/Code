string = str(input("Enter a word or a sentence: "))
string2 = ""
for i in range(-1, -len(string)-1, -1):
    string2 += string[i]
print("Reversed string:", string2)