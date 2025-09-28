# 1. Python program to find whether the given number is Even or Odd
while True:
    try:
        n = int(input("n: "))
        break
    
    except ValueError:
        print("Please enter a number!")

print(f"{n} is even.") if n%2 == 0 else print(f"{n} is odd.")