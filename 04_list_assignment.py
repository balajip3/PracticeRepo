# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
# Your code here

square_numbers = []
for i in range(1,11):
  result = int(i*i)
  
  square_numbers.append(result)
print("First 10 square numbers :",square_numbers)

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here

a = [1,2,3,4,5,6,7,8,9,10]

sum = 0 

for i in a:
  if i%2 == 0:
    sum = sum + i 
print(sum)

# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here

a = [1,2,2,3,4,4,5,6,6,7]
b = set(a)
c = list(b)
print(c)

# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here

a = [64,34,25,12,22,11,90]

a.sort(reverse = True)
print(a)

# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here

a = [15,23,31,42,56,78,91]

length = len(a)

sum = 0 

for i in a:
  sum = sum + i 
print(sum/length)


# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here

result = [0,1]

for i in range(13):
  next_num = result[-1] + result[-2]
  result.append(next_num)
print(result)

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here

a = [45,67,23,89,12,34,78]
a.sort(reverse = True)
print("second largest number :", a[1])

# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.reverse()
print(a)

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here

a = [1,5,2,5,3,5,4,5,6]

print(a.count(5))



# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here

a = []

for i in range(1,51):
  if i < 2:
    continue 
  is_valid = True 
  for j in range(2,i):
    if (i%j == 0):
      is_valid = False
      break
  if is_valid:
    a.append(i)
print(a)
    

# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []

for i in a:
  if type(i) == list:
    for x in i:
      result.append(x)
  else:
    result.append(i)
print(result)


# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here

a = [1,2,3,4,5]

b = [4,5,6,7,8]

result = []

for i in a:
  if i in b:
    result.append(i)
print(result)



# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here

a = [1,2,3,4,5,6]

result = [] 

for i in range(0,len(a),2):
  result.append([a[i], a[i+1]])
print(result)


# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in a:
  print(sum(i))

       [OR] 

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in a:
  total = 0 
  for num in i:
    total = total + num 
  print(total)


# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []

for i in range(3):
  new_row = []
  for j in range(3):
    new_row.append(a[i][j])
  result.append(new_row)
print(result)
                  

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here

a = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]

for i in a:
  print("Maximum value in each sublist :", max(i))

# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

for i in a:
  for j in i:
    for num in j:
      print(num, end=" ")
    print()
  print("---")


# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

total = 0 

for i in a:
  for j in i:
    for num in j:
      total = total + num 
print("sum of all elements :", total)




# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []
for i in a:
  for j in i:
    if j%2 == 0:
      result.append(j)
print(result)


# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here

a = [1, 'hello', 3.14, True, [1, 2, 3]]
print(a)

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here

a = ['apple', 'banana', 'cherry', 'date']

result = [] 
for i in a:
  result.append(len(i))
print(result)

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

a = [(1, 'a'), (2, 'b'), (3, 'c')]
print(a)

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

a = [(1, 'a'), (2, 'b'), (3, 'c')]

result = []
for i in a:
  result.append(i[0])
print(result)

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here

a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}] 
print(a) 


# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here

a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
result = []

for i in a:
  result.append(i["name"])
print(result)

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here

a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
result = a[0]

for i in a:
  if i["age"] > result["age"]:
    result = i 
print(result)

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here

a = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

print(a)


# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here

a = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

result = 0 

for i in a:
  for j in i:
    for num in j:
      for maximum in num:
        if maximum > result:
          result = maximum 
print(result)

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here

a = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(a)

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here

a = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]

b = set()

for i in a:
  for j in i:
    b.add(j)
print(b)

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here

a = [1+2j, 3+4j, 5+6j]
print(a)


# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here

a = [1+2j, 3+4j, 5+6j]

for i in a:
  real = i.real
  image = i.imag 
  result = (real * real  + image * image ) ** 0.5 
  print(result)



# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

a = [1, [2, 3], [4, [5, 6]], 7]
print(a)


# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
a = [1, [2, 3], [4, [5, 6]], 7]

depth = 1 

for i in a:
  if isinstance(i,list):
    if depth < 2:
      depth = 2 

    for sub in i:
      if isinstance(sub, list):
        if depth < 3:
          depth = 3 
print(depth)


# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here

a = [len, str, int, float]

print(a)

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here

a = [len, str, int, float]

for i in a:
  print(i("1234"))

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here

a = [lambda x: x*2, lambda x: x**2, lambda x: x+1]

print(a) 


# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here

a = [lambda x: x*2, lambda x: x**2, lambda x: x+1]

for i in a:
  print(i(5))



# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here

a = [list, dict, set, tuple]
print(a)

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here

a = [list, dict, set, tuple]
for i in a:
  if i == dict:
    instance = i()
  else:
    instance = i([1,2,3])
  print(instance)

# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here

a = [None, None, None, None]
print(a)

# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here

a = [None, None, None, None]

for i in range(len(a)):
  if a[i] is None:
    a[i] = 0 
print(a)



# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here

a = [True, False, True, False]
print(a)

# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here

a = [True, False, True, False]
print(a.count(True))

       [OR]

a = [True, False, True, False]

count = 0 

for i in a:
  if i == True:
    count = count + 1
print(count)


# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here

a = [range(3), range(5), range(2)]
print(a)


# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
# Your code here

a = [range(3), range(5), range(2)]

result = []

for i in a:
  result.append(list(i))
print(result)

# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here

a = [(x for x in range(3)), (x for x in range(5))]

print(a)


# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here

a = [(x for x in range(3)), (x for x in range(5))]

b = [list(x) for x in a]
print(b)

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here

a = [iter([1, 2, 3]), iter([4, 5, 6])]
print(a)

# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 

a = [iter([1, 2, 3]), iter([4, 5, 6])]

result = []

for i in a:
  result.append(list(i))
print(result)
