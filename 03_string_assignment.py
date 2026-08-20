# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# Your code here
name = input()
reverse_string = name[::-1]
print(reverse_string)

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here
name = input()
reverse_string = name[::-1]
if name == reverse_string:
  print("Palindrome")
else:
  print("Not a Palindrome")
  

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# Your code here
name = input()
words = name.split()
length = len(words)
print(length)

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
name = input()
name_title = name.title()
print(name_title)

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
name = input()
length_string = len(name)
print(length_string)

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
name = input()
replace = name.replace(" ", "_")
print(replace)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
name = input()
words = name.split()
if "Python" in words:
  print("Yes")
else:
  print("No")
    
# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
name = input()
characters = name[0:5]
print(characters)

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
name = input()
lowercase = name.lower()
print(lowercase)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
name = input()
words = "" 
for i in name:
  if i.lower() not in "aeiou":
    words = words + i 
print(words)
# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
first_name = "listen"
second_name = "silent"
first_length = len(first_name)
second_length = len(second_name)
if first_length != second_length:
  print("No")
elif sorted(first_name) == sorted(second_name):
  print("Anagrams")
else:
  print("No")
  
# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
name = input()
capital_name = name.title()
print(capital_name)

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
name = input()
count = ""
for char in name:
  if char != " " and char.lower() not in "aeiou":
    count = count + char
print(len(count))

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
name = input()
words = name.split() 

longest_word = ""

for char in words:
  if len(char) > len(longest_word):
    longest_word = char 
print(longest_word)


# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
name = input()
result = ""

for char in name:
  if char.isalpha() or char == " ":
    result = result + char 
print(result)


# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
name = input()

result = name.startswith("Python")
print(result)

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
name = input() 
result = name.index("o")
print(result)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
name = input()
result = name.split(",")
print(result)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here
name = ['Python', 'is', 'awesome']
result = " ".join(name)
print(result)

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
number = input()
result = number.isnumeric()
print(result)


# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
name = input()
result = name.isalpha()
print(result)

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
name = "banana"
result = []

for i in range(len(name)):
  if name[i] == "a":
    result.append(i)
print(result)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
name = " Hello World "
result = name.strip()
print(result)

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
name = input()
result = name.endswith("ing")
print(result)

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
name = input()
result = name.replace("o","0",1)
print(result)

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here
name = "Python is a programming language"
words = name.split()

result = words[0]

for char in words:
  if len(char) < len(result):
    result = char 
print(result)

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
name = "Python programming is powerful"
words = name.split()

result = 0 

for char in words:
  counter = char.startswith("p")
  if counter == True:
    result = result + 1 
print(result)
                            


# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
name = "Hello World Python"
words = name.split()
result = words[::-1]
final = " ".join(result)
print(final)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here



# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here
name = "https://www.example.com/path"
words = name.split("://") 
result = name.split("/")

for char in result:
  if char.startswith("www"):
    print(char)

     [OR]

name = "https://www.example.com/path"
result = name.split("://")[1].split("/")[0]
print(result)




# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here

text = """ Wake up with purpose and chase your goals today.
Push hard because your success depends on your own actions.
Ignore doubt and trust your inner strength to win.
Keep moving forward no matter how hard things get."""

result = len(text.splitlines())
print("Count lines :", result)



# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here
first_word = "hello"
second_word = "world"

result = " "

for char in first_word:
  if char in b and char not in result:
    result = result + char 
print(result)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here
input_name = "abc123def456ghi789"

result = " "

for i in input_name:
  if i.isdigit():
    result = result + i 
print(result)

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here
name = "snake_case"

words = name.split("_")
print(words)


# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here
word = "A man a plan a canal Panama"

words = word.lower().replace(" ","")

result = words[::-1]

if words == result:
  print("Valid palindrome")
else:
  print("Not a palindrome")


# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here

name = "the quick brown fox jumps over the lazy dog"

words = name.split()
count = {}

for word in words:
  if word in count:
    count[word] = count[word] + 1 
  else:
    count[word] = 1 
most_common_word = max(count, key=count.get)
print("Words counts :", count)
print("Most common word :", most_common_word)

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here

name = "National Aeronautics and Space Administration"

words = name.split()
result = ""

for char in words:
  if char[0].isupper():
    result = result + char[0]
print(result)

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 
