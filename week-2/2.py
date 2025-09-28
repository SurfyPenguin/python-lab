# 2. Python Program to Calculate the Area and Perimeter of Triangle and Circle.
from math import pi

def float_input(string):
    while True:
        try:
            n = float(input(string))
            return n

        except ValueError:
            print("Please enter a number!")

def area_of_triangle(base, height):
    return 0.5 * base * height

def perimeter_of_triangle(s1, s2, s3):
    return s1 + s2 + s3

def area_of_circle(radius):
    return pi * radius ** 2

def perimeter_of_circle(radius):
    return pi * 2 * radius

option = input("1. Area of triangle\n"
               "2. Perimeter of triangle\n"
               "3. Area of circle\n"
               "4. Perimeter of circle\n"
               ":").strip()

if option == "1":

    base = float_input("Base: ")
    height = float_input("Height: ")

    print("Area of triangle:", area_of_triangle(base, height))

elif option == "2":

    side_1 = float_input("Side 1: ")
    side_2 = float_input("Side 2: ")
    side_3 = float_input("Side 3: ")

    print("Perimeter of triangle:", perimeter_of_triangle(side_1, side_2, side_3))

elif option == "3":

    radius = float_input("Radius: ")

    print("Area of circle:", area_of_circle(radius))

elif option == "4":

    radius = float_input("Radius: ")

    print("Perimeter of circle:", perimeter_of_circle(radius))

else:
    print("Invalid option!")