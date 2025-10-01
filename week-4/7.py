# 7. Write a python program to count total number of notes in given amount

while True:
    try:
        amount = int(input("n: "))
        break

    except  ValueError:
        print("Please enter a number!")

denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

notes = {}

for note in denominations:

    if amount >= note:
        n = amount // note
        notes[note] = n

    amount %= note

print("Required Notes:")
for i in notes:
    print(f"{i} : {notes[i]}")