# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
# Your code here

a = {1,2,3,4,5,6,7,8,9,10}

print(a)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
# Your code here

a = {1,2,3,4,5}
a.add(11)
print(a)


# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
# Your code here

a = {1,2,3,4,5,6}

a.remove(3)

print(a)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here

a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}

c = a.intersection(b)

print(c)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here

a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}

c = a.difference(b) 

print(c)



# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
# Your code here

a = {1, 2, 3, 4, 6, 7, 8}

if 5 in a:
  print("True")
else:
  print("False")

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
# Your code here

a = {'a', 'b', 'c', 'd', 'e'}

b = len(a)

print(b)

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
# Your code here

a = "hello world"

result = set()

for i in a:
  if i != " " and i not in "aeiou":
    result.add(i) 
print(result)


# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
# Your code here

a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

b = set(a)

print(b)


# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
# Your code here 

a = {1,2,3}

b = {1,2,3,4,5,6}

a.issubset(b)
