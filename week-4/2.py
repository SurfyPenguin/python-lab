# 2. Write a python program to check whether a number is divisible by 5 and 11 or not.

while True:
    try:
        n = int(input("n: "))
        break

    except  ValueError:
        print("Please enter a number!")

if n%5 == 0 and n%11 == 0:
    print(f"{n} is divisible by both 5 & 11.")

else:
    print(f"{n} is not divisible by both 5 & 11")
