PYTHON NOTES

1. List
• A list is an ordered and mutable collection.
• Allows duplicate values.
• Written using [] brackets.

Example:
list1 = [10, 20, 30, 20]
print(list1)

------------------------------------

2. Tuple
• A tuple is an ordered and immutable collection.
• Allows duplicate values.
• Written using () brackets.

Example:
tuple1 = (10, 20, 30, 20)
print(tuple1)

------------------------------------

3. Set
• A set is an unordered and mutable collection.
• Does not allow duplicate values.
• Written using {} brackets.

Example:
set1 = {10, 20, 30, 20}
print(set1)

Output:
{10, 20, 30}

------------------------------------

4. Dictionary
• A dictionary stores data as key:value pairs.
• Keys must be unique.
• Written using {} brackets.

Example:
student = {
    "Name": "Lokesh",
    "Age": 21,
    "Course": "Python"
}
print(student)

------------------------------------

5. Nested List
• A nested list is a list inside another list.
• Used to store data in rows and columns.

Example:
nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested)
print(nested[1][2])   # Output: 6