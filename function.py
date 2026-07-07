# TASK:03/06/2026 - Functions

# 1. Addition
def add(a, b):
    return a + b
print("Addition:", add(10, 20))

# 2. Subtraction
def sub(a, b):
    return a - b
print("Subtraction:", sub(20, 10))

# 3. Multiplication
def mul(a, b):
    return a * b
print("Multiplication:", mul(5, 4))

# 4. Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print("17 is", even_odd(17))

# 5. Factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
print("Factorial:", factorial(5))

# 6. Prime Number
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print("13 is", prime(13))

# 7. Reverse String
def reverse(s):
    return s[::-1]
print("Reverse:", reverse("Python"))

# 8. Maximum of Two Numbers
def maximum(a, b):
    return a if a > b else b
print("Maximum:", maximum(25, 40))

# 9. Square
def square(n):
    return n * n
print("Square:", square(6))

# 10. Cube
def cube(n):
    return n * n * n
print("Cube:", cube(3))