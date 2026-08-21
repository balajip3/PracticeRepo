# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
# Your code here
a = 1 

for i in range(1,11):
  a = a * i 
print("product of first 10 natural numbers :", a)


# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
a = 156 
b = 7 

remainder = a / b 
print("remainder :", remainder)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
a = 25 
b = a ** 2 
print("Square of 25 :",b)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here

a = 125 

for i in range(1,a+1):
  if i*i*i == a:
    print("Cube root of 125 :", i)
    break

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
numbers = "12345"
count = 0 

for i in numbers:
  count = count + int(i) 
print("Sum of digits in number 12345 :", count)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
a = 97
is_prime = True

if a < 2:
  is_prime = False
else:
  for i in range(2,a):
    if (a%i) == 0:
      is_prime = False
      break
if is_prime:
  print(a , "is a Prime Number")
else:
  print(a , "is not a Prime Number")
    
    

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
a = 8 
result = 1 
for i in range(1,a+1):
  result = result * int(i)
print("Factorial of 8:", result)

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
numbers = [15,23,31,42,56]
length = len(numbers)

count = 0 
for i in numbers:
  count = count + int(i)
print("Average of Numbers 15,23,31,42,56 :", count/length)


# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
import math
math.gcd(48,36)

     [OR]

a = 48 
b = 36 

first_value = []
second_value = []

for i in range(1,a+1):
  if a%i == 0:
    first_value.append(i)
for j in range(1,b+1):
  if b%j == 0:
    second_value.append(j)
common = []
for x in first_value:
  if x in second_value:
    common.append(x)
gcd = max(common)
print("Greatest Common Divisor :", gcd)
    
  


# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 
sum = 0 
for i in range(1,40):
  if i%2 != 0:
    sum = sum + i 
print(sum)
