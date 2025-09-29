# 3. Write a python program to check whether a character is alphabet or not.

while True:
    c  = input("Character: ")

    if len(c) > 1:
        print("Please enter a single character!")
        continue
    break

if c.isalpha():
    print(f"{c} is an alphabet.")

else:
    print(f"{c} is not an alphabet.")