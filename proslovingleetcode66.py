
digits = list(map(int, input("Enter digits separated by space: ").split()))

num = int("".join(map(str, digits)))
num += 1

result = list(map(int, str(num)))

print("Output:", result)