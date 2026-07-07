# TASK: Find Input and Output Function Errors

# 1. Error: input without quotes
# name = input(Enter your name)
# Correct:
name = input("Enter your name: ")

# 2. Error: Missing closing bracket
# age = input("Enter age: "
# Correct:
age = input("Enter age: ")

# 3. Error: Adding string with integer
# print("Age = " + 20)
# Correct:
print("Age =", 20)

# 4. Error: input returns string
# age = input("Enter age: ")
# print(age + 5)
# Correct:
age = int(input("Enter age: "))
print(age + 5)

# 5. Error: Misspelled print
# pritn("Hello")
# Correct:
print("Hello")

# 6. Error: Misspelled input
# inpt("Enter value: ")
# Correct:
value = input("Enter value: ")

# 7. Error: Using undefined variable
# print(name1)
# Correct:
print(name)

# 8. Error: Missing comma in print
# print("Hello" "World")
# Better:
print("Hello", "World")

# 9. Error: Invalid int conversion
# num = int(input("Enter number: "))
# If user enters abc -> ValueError
# Correct:
# Enter only numbers

# 10. Error: Missing quotes in print
# print(Hello)
# Correct:
print("Hello")