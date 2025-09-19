# 3. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

try:
    n = int(input("n: "))
    str_n = str(n)
    value = int(str_n) + int(str_n*2) + int(str_n*3)
    print("n + nn + nnn =", value)

except ValueError:
    print("Please enter an integer!")