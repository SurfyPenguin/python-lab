# 3. Write a Python program to test whether a number is within 100 or 1000 or 2000.

while True:
    try:
        n = int(input("n: "))
        if n < 0:
            print("Please enter a positive number!")
            continue
        break

    except ValueError:
        print("Please enter a number!")

if n <= 100:
    print("Within 100")

elif n <= 1000:
    print("Within 1000")

elif n <= 2000:
    print("Within 2000")

else:
    print("Greater than 2000")