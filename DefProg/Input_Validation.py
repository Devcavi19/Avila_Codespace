import re

name = input("Enter name: ")


def check_input(name):
    if name == "":
        raise ValueError("Input is empty.")

def str_length(name):
    if not 3 <= len(name) <= 20:
        raise ValueError("Input must be 3-20 characters long")

def validate(name):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])[A-Za-z\s]+$'
    if not re.match(pattern, name):
        raise ValueError("Name can not be mixed with any numbers and special characters")
    else:
        print("Name is validated")

try:
    check_input(name)
    str_length(name)
    validate(name)
except ValueError as e:
    print(e)