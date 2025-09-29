# 7. Write a python program to find whether a given year is leap or not.

while True:
    try:
        year = int(input("Year: "))
        break

    except ValueError:
        print("Please enter a valid year!")

if year%4 == 0:
    print(f"{year} is a leap year!")

else:
    print(f"{year} is not a leap year!")