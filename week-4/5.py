# 5. Write a python program to check whether a character is uppercase or lowercase alphabet.

while True:

    char = input("Character: ")
    if len(char) > 1:
        print("Enter a single character!")
        continue
    break

if char.isalpha():

    if char.isupper():
        print("Uppercase!")
    else:
        print("Lowercase!")

else:
    print(f"{char} is not an alphabet.")