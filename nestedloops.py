# TASK:19/06/2026

# 1. Sum of Digits
n = 1234
s = 0
t = n
while t > 0:
    s += t % 10
    t //= 10
print("Sum of Digits:", s)

# 2. Reverse a Number
n = 1234
rev = 0
t = n
while t > 0:
    rev = rev * 10 + t % 10
    t //= 10
print("Reverse:", rev)

# 3. Count Digits
n = 12345
count = 0
t = n
while t > 0:
    count += 1
    t //= 10
print("Count Digits:", count)

# 4. Check Even or Odd
n = 17
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5. Check Prime Number
n = 13
prime = True
if n <= 1:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")

# 6. Find Factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 7. Find Factors
n = 12
print("Factors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 8. Check Palindrome Number
n = 121
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 9. Check Armstrong Number
n = 153
temp = n
length = len(str(n))
arm = 0

while temp > 0:
    digit = temp % 10
    arm += digit ** length
    temp //= 10

if arm == n:
    print("Armstrong")
else:
    print("Not Armstrong")

# 10. Find GCD (HCF)
a = 12
b = 18

while b != 0:
    a, b = b, a % b

print("GCD:", a)