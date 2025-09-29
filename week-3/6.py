# 6. Python Program to print maximum of 3 numbers

while True:
    try:
        n1 = int(input("number 1: "))
        n2 = int(input("number 2: "))
        n3 = int(input("number 3: "))
        break

    except:
        print("Please enter a number!")

max = max(n1, n2, n3)
print("Max:", max)