# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
a = [3.14,2.718,1.618,0.577]
b = sum(a)/len(a)
print("Average :", b)

      [OR]

a = "3.14,2.718,1.618,0.577"
b = a.split(",")
c = len(b) 

count = 0 

for i in b:
  count = count + float(i)
print("Average :", count)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
### Fahrenheit to Celsius formula 
### c = (f - 32) * 5/9 
f = 98.6 
c = (f - 32) * 5/9 
print(c)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here

### compound interest formula 
### amount = p * (1 + r/100) ** t 
### interest = amount - p 

p = 1000
r = 5.5 
t = 3

amount = p * (1 + r/100) ** t
print("Total Amount :",round(amount,2))

interest = amount - p 
print("Interest :", round(interest,2))

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here

### hypotenuse of a right triangle 
### h = root( a ** 2 + b ** 2
a = 3.5 
b = 4.2 

c = a ** 2 + b ** 2 

h = c ** 0.5 
print("hypotenuse of a right triangle :", round(h,2))

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here

###formula V = (4/3)_pi_r**3 
import math
V = (4/3) * math.pi * r **3 
print("volume of a sphere with radius 7.8 :", round(V,2))

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here

print(round(3.14159,3))

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here

### formula percentage = (part/whole) * 100
part = 45
whole = 67
percentage = (part/whole) * 100 

print(round(percentage,2))

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here

import math 

a = 23.456 
root = math.sqrt(a)
print(round(root,4))


# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here

### formula SI = (P*R*T)/100 

P = 2500 
R = 6.5 
T = 2.5 

SI = (P*R*T)/100
print(SI)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 

### formula radians = degrees * (pi/180)
import math
degrees = 45.7 

formula = 45.7 * (math.pi/180)
print(round(formula,4))
