# 6. Python Program to Convert Celsius To Fahrenheit
try:
    temp = float(input("Temperature (°C): "))
    converted_temp = (temp * 9/5) + 32
    print(f"Temperature (°F): {converted_temp}")

except ValueError:
    print("Please enter a number!")