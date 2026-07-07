# Bitwise Operators in Python
a = 10
b = 10
c = 5
print("BITWISE OPERATORS IN PYTHON")
print("-" * 40)

# 1. AND (&)
print("1. AND (&)")
print(f"{a} & {c} = {a & c}")

# 2. OR (|)
print("\n2. OR (|)")
print(f"{a} | {c} = {a | c}")

# 3. XOR (^)
print("\n3. XOR (^)")
print(f"{a} ^ {c} = {a ^ c}")

# XOR with same values
print("\nXOR of Same Values")
print(f"{a} ^ {b} = {a ^ b}")
print("Output is 0 because both values are same.")

# 4. NOT (~)
print("\n4. NOT (~)")
print(f"~{a} = {~a}")

# 5. Left Shift (<<)
print("\n5. Left Shift (<<)")
print(f"{a} << 2 = {a << 2}")

# 6. Right Shift (>>)
print("\n6. Right Shift (>>)")
print(f"{a} >> 2 = {a >> 2}")

# Check Even or Odd using Bitwise AND
print("\nChecking Even or Odd using Bitwise AND")

num = 1

if num & 1:
    print(f"{num} is Odd")
else:
    print(f"{num} is Even")