# TASK:19/05/2026

# 1. Print given value is Positive or Not
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Given Character is Upper Case or Lower Case
# (Without using built-in functions)

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Upper Case")
elif 'a' <= ch <= 'z':
    print("Lower Case")
else:
    print("Not an Alphabet")

# 3. Pass or Fail (6 Subjects)

s1 = int(input("Enter Subject1 Marks: "))
s2 = int(input("Enter Subject2 Marks: "))
s3 = int(input("Enter Subject3 Marks: "))
s4 = int(input("Enter Subject4 Marks: "))
s5 = int(input("Enter Subject5 Marks: "))
s6 = int(input("Enter Subject6 Marks: "))

if s1 > 35 and s2 > 35 and s3 > 35 and s4 > 35 and s5 > 35 and s6 > 35:
    print("PASS")
else:
    print("FAIL")
    