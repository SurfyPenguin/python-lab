# 6. Write a python program to input week number and print week day.

week = {
    "1" : "monday",
    "2" : "tuesday",
    "3" : "wednesday",
    "4" : "thursday",
    "5" : "friday",
    "6" : "saturday",
    "7" : "sunday",
}

n = input("n: ")

if n in week:
    print(week[n])

else:
    print("Doesn't exist!")