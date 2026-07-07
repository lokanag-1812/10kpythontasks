# TASK:12/06/2026
# Armstrong Number

num = int(input("Enter a number: "))

temp = num
length = len(str(num))
sum = 0

print("Length =", length)
print("Digits:")

while temp > 0:
    digit = temp % 10
    print(digit)
    sum = sum + digit ** length
    temp = temp // 10

print("Sum =", sum)

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")