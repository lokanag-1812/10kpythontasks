# TASK:07/02/2026

# 1. LeetCode 2544 - Alternating Digit Sum

n = int(input("Enter a number: "))
digits = str(n)

sum = 0
sign = 1

for d in digits:
    sum = sum + sign * int(d)
    sign = -sign

print("Alternating Digit Sum =", sum)


# 2. LeetCode 2553 - Separate the Digits in an Array

arr = list(map(int, input("Enter array elements: ").split()))

result = []

for num in arr:
    for digit in str(num):
        result.append(int(digit))

print("Separated Digits =", result)