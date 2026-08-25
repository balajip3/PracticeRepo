# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
# Your code here

students = {
  "Balaji" : 26,
  "Raju" : 28,
  "Ramu" : 23
}

print(students)

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
# Your code here

my_dict = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}


my_dict["d"] = 4 
print(my_dict)


# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
# Your code here

a = {'name': 'John', 'age': 25, 'city': 'New York'}

print(a.keys())




# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
# Your code here

a = {'python': 3, 'java': 2, 'c++': 1}

print(a.values())

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
# Your code here

a = {'name': 'Alice', 'age': 30, 'city': 'London'}

if "age" in a:
  print("key is available")
else:
  print("key is not available")


# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
# Your code here

a = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}

del a["temp"]
print(a)

# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
# Your code here

a = {'math': 85, 'science': 92, 'english': 78}

b = a.values()

print(sum(b))

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
# Your code here

a = {} 

for i in range(1,6):
  a[i] = i * i 
print(a)

# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
# Your code here

a = "hello"

b = {}

for i in a:
  b[i] = a.count(i)
print(b)

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
# Your code here

a = {'a': 1, 'b': 2}

b = {'c': 3, 'd': 4}

print(a | b)

# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
# Your code here

a = {'person': {'name': 'Alice', 'age': 25}}

print(a)

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
# Your code here

a = {'person': {'name': 'Alice', 'age': 25}}

b = a["person"]["name"]

print(b)

# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
# Your code here

a = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}

print(a)

# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
# Your code here

a = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
a["fruits"].append("orange")
print(a)

# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
# Your code here

a = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(a)

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
# Your code here

a = {'coordinates': (10, 20), 'rgb': (255, 0, 0)} 

b = a["coordinates"]

print(b[0])

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
# Your code here

a = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}

print(a)

# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
# Your code here

a = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}

a["vowels"].add("o")

print(a)

                

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
# Your code here

a = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}

print(a)


# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
# Your code here

a = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}

b = a["company"]["department"]["employee"]["name"]

print(b)

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
# Your code here

a = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}

print(a)


# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
# Your code here

a = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}

b = a.values()

for i in b:
  print(type(i))


# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
# Your code here

a = {'len': len, 'str': str, 'int': int}

b = a.values()

for i in a:
  print(i)

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
# Your code here

a = {'len': len, 'str': str, 'int': int}

for i in a.values():
  print(i("123"))

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
# Your code here

a = {'double': lambda x: x*2, 'square': lambda x: x**2}

print(a)

     

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
# Your code here

x = 5
a = {'double': lambda x: x*2, 'square': lambda x: x**2}

for i in a.values():
  print(i(x))


# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
# Your code here

a = {'list': list, 'dict': dict, 'set': set}

print(a)

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
# Your code here

a = {'list': list, 'dict': dict, 'set': set}

print(a["list"](), a["dict"](), a["set"]())



# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
# Your code here

a = {'a': None, 'b': None, 'c': None}

print(a)

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
# Your code here

a = {'a': None, 'b': None, 'c': None}

for i in a:
  if a[i] is None:
    a[i] = 0 
print(a)


# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
# Your code here

a = {'is_active': True, 'is_admin': False}

print(a)

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
# Your code here

a = {'is_active': True, 'is_admin': False}

count = 0 

for i in a.values():
  if i is True:
    count = count + 1
print(count)


# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
# Your code here

a = {'z1': 3+4j, 'z2': 1+2j}

print(a)


# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
# Your code here

a = {'z1': 3+4j, 'z2': 1+2j}

for k,v in a.items():
  print(abs(v))




# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
# Your code here

students = {
  "cse" : {
    "3rd year" : {
      "section A" : {
        "Strength" : 60 
      }
    }
  }
}

print(students)


# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
# Your code here

students = {
  "cse" : {
    "3rd year" : {
      "section A" : {
        "Strength" : 60 
      }
    }
  }
}

print(students["cse"]["3rd year"]["section A"]["Strength"])


# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
# Your code here

a = {'r1': range(3), 'r2': range(5)}

print(a)

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
# Your code here

a = {'r1': range(3), 'r2': range(5)}

for k,v in a.items():
  print(k, ":", list(v))

# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
# Your code here

a = {
  "g1" : (x for x in range(3)),
  "g2" : (x*x for x in range(5))
}

print(a)
print(a["g1"])
print(list(a["g1"]))
  
  

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
# Your code here

b = {}

for k , v in a.items():
  b[k] = list(v)
print(b)

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
# Your code here

a = {
  "i1" : iter([0,1,2]),
  "i2" : iter([0,1,4,9,16])
}

for i in a.values():
  print(type(i))


# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
# Your code here

a = {
  "i1" : iter([0,1,2]),
  "i2" : iter([0,1,4,9,16])
}

for k,v in a.items():
  print(k, ":", list(v))
  

# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
# Your code here

a = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}

print(a)

# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
# Your code here

a = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}

for row in a["matrix"]:
  print(f"{row} sum = {sum(row)}")
print(f"{a["vector"]} sum = {sum(a["vector"])}")


total = sum(a["vector"]) + sum(sum(row) for row in a["matrix"])
print("total sum :", total)

# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
# Your code here

a = {'config': {'db': {'host': 'localhost', 'port': 5432}}}

print(a)

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
# Your code here

a = {'config': {'db': {'host': 'localhost', 'port': 5432}}}

print(a["config"]["db"]["port"])


# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
# Your code here

a = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}

print(a)

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
# Your code here

a = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}

print(a["points"][0])

# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
# Your code here

a = {
    'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})}, 
    'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}
    }

print(a)

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
# Your code here 

a = {
    'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})}, 
    'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}
    }
all_union = set().union(*a["groups"], *a["categories"])
print(all_union)



