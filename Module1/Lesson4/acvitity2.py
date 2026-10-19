amount = input("How much did you withdraw?: ")
amount = int(amount)

note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = ((amount % 100) % 50) // 10

print("You will receive:")
print(note_1, "notes of 100")
print(note_2, "notes of 50")
print(note_3, "notes of 10")