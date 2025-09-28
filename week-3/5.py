# 5. Python Program to Find the Factorial of a Number

while True:
    try:
        n = int(input("n: "))

        if n < 0:
            print("Please enter a positive number!")
            continue
        break
    
    except ValueError:
        print("Please enter a number!")

# alt approach
def factorial(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial(n-1)
    
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
