# Type Conversion in Python (24 Examples)

print(int(10.5))            # 1. float -> int
print(int(True))            # 2. bool -> int
print(int("25"))            # 3. str -> int

print(float(10))            # 4. int -> float
print(float(True))          # 5. bool -> float
print(float("12.5"))        # 6. str -> float

print(str(100))             # 7. int -> str
print(str(12.5))            # 8. float -> str
print(str(True))            # 9. bool -> str

print(bool(0))              # 10. int -> bool
print(bool(1))              # 11. int -> bool
print(bool(""))             # 12. str -> bool
print(bool("Python"))       # 13. str -> bool

print(list("Python"))       # 14. str -> list
print(tuple("Python"))      # 15. str -> tuple
print(list((1,2,3)))        # 17. tuple -> list
print(tuple([1,2,3]))       # 18. list -> tuple
print(set([1,2,2,3]))       # 19. list -> set

print(list({1,2,3}))        # 20. set -> list
print(tuple({1,2,3}))       # 21. set -> tuple

print(dict([("a",1),("b",2)]))      # 22. list -> dict
print(list({"a":1,"b":2}))          # 23. dict -> list (keys)
print(tuple({"a":1,"b":2}))         # 24. dict -> tuple (keys)