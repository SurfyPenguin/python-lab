#1. Python Program to Find the Square Root
from math import sqrt

try:
    n = float(input("Enter a number: "))
    print(sqrt(n))

except ValueError:
    print("Please enter an int or a float value!")