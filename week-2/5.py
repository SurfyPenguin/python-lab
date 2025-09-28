# 5. Python Program to Convert Kilometres to Miles

try:
    n = float(input("Value in kilometres: "))
    print(f"Value in miles: {n/1.61:.2f}")

except ValueError:
    print("Please enter a number!")