# TASK:19/06/2026

# 1. Sum of Digits
n = 1234
s = 0
t = n
while t > 0:
    s += t % 10
    t //= 10
print("Sum of Digits =", s)

# 2. Reverse a Number
n = 1234
rev = 0
t = n
while t > 0:
    rev = rev * 10 + t % 10
    t //= 10
print("Reverse =", rev)

# 3. Count Digits
n = 12345
count = 0
t = n
while t > 0:
    count += 1
    t //= 10
print("Count Digits =", count)

# 4. Even or Odd
n = 17
print("Even" if n % 2 == 0 else "Odd")

# 5. Prime Number
n = 13
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print("Prime" if prime else "Not Prime")

# 6. Factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# 7. Factors
n = 12
print("Factors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 8. Palindrome Number
n = 121
t = n
rev = 0
while t > 0:
    rev = rev * 10 + t % 10
    t //= 10
print("Palindrome" if n == rev else "Not Palindrome")

# 9. Armstrong Number
n = 153
length = len(str(n))
t = n
s = 0
while t > 0:
    d = t % 10
    s += d ** length
    t //= 10
print("Armstrong" if s == n else "Not Armstrong")

# 10. GCD (HCF)
a = 12
b = 18
while b != 0:
    a, b = b, a % b
print("GCD =", a)