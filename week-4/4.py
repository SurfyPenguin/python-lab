# 4. Write a python program to input any character and check whether it is alphabet, digit or special character.

while True:

    char = input("Character: ")
    if len(char) > 1:
        print("Enter a single character!")
        continue
    break

if char.isalpha():
    print(f"{char} is an alphabet.")

elif char.isdigit():
    print(f"{char} is a digit.")

else:
    print(f"{char} is a special character.")