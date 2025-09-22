# 3. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

try:
    n = input("n: ")
    value = int(n) + int(n*2) + int(n*3)
    print("n + nn + nnn =", value)

except ValueError:
    print("Please enter an integer!")