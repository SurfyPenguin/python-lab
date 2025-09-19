# 1. Write a Python program to display the current date and time.
from datetime import datetime
current_date_time = datetime.now()

new_date_time = current_date_time.strftime("%d-%m-%Y :: %H:%M:%S")
print("Date and time:", new_date_time)
