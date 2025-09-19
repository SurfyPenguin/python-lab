# 2. Write a Python program to get the Python version you are using
import subprocess

command = ["python", "--version"]
subprocess.run(command)