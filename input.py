# This program collects user information and displays it back to them.
# name, address, age, and salary are collected from the user.

Name = input("Enter your name: ")
Address = input("Enter your address: ")
Age = input("Enter your age: ")
salary = input("Enter your salary: ")
print("\nThank you for providing your information!\n")
print("--------------------------")
print(f"Hello, {Name}!")
print(f"Your address is: {Address}")
print(f"Your age is: {Age}")
print(f"Your salary is: {salary}")