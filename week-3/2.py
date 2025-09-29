# 2. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

while True:
    try:
        n = int(input("n: "))
        break
    except ValueError:
        print("Please enter a number!")

diff = 17 - n

if n > 17:
    print(2*(abs(diff)))
else:
    print(diff)