from math import sqrt

while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        break

    except ValueError:
        print("Please enter a number!")

discriminant = b**2 -  4*a*c

if discriminant > 0:
    print("Roots are real and distinct")
    root1, root2 = (b + sqrt(discriminant))/2*a, (b - sqrt(discriminant))/2*a
    print(f"alpha = {root1:.2f}, beta = {root2:.2f}")

elif discriminant == 0:
    print("Roots are real and equal")
    root = (b + sqrt(discriminant))/2*a
    print(f"alpha = beta = {root}")

else:
    print("Roots are imaginary")
    root1, root2 = complex(b/2*a, sqrt(abs(discriminant))/2*a), complex(b/2*a, -sqrt(abs(discriminant))/2*a)
    print(f"alpha = {root1.real} + {root1.imag:.2f}j, beta = {root2.real} - {abs(root1.imag):.2f}j")