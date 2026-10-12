# 1. Write a Python program to print the length of the string "Python".

str1 = "python"
print(len(str1))

# 2. Write a program to print the first and last characters of "Programming" using positive indexing.

str2 = "Programming"
print(len(str2))
print(str2[0])
print(str2[10])

#3. Find the output.

s = "Computer"
print(s[2])
print(s[5])
print(len(s))

# 4. Write a program to print the first three characters of "Education" using positive indexing.

str3 = "Education"
print(str3[0:3])

# 5. Find the output.
s = "Hello World"
print(s[-1])
print(s[-3])
print(len(s))

# 6. Write a program to print the second character from the beginning and the second character from the end of "Developer".
str4 = "Developer"
print(str4[1:7])
print(len(str4))

# 7. Find the output.
s = "Python Programming"
print(s[7])
print(s[-7])
print(len(s))

#8. Write a program to print the middle character of "Python" using len() and indexing.

str5 = "python"
print(str5[(len(str5) // 2)])

#9. Find the output.
s = "Kiran Academy"
print(s[5])
print(s[-5])
print(s[0])
print(s[-1])

#10. Write a program to accept a string from the user and print its length, first character, and last character.

str6 = input("enter string -")
print(len(str6))
print(str6[0])
print(str6[-1])

#11. Find the output.
s = "Artificial Intelligence"
print(len(s))
print(s[10])
print(s[-10])

# 12. Write a program to print the third character from the beginning and the third character from the end of "Information".
str7 = "information"
print(str6[2])
print(str6[-3])


#13. Find the output.
s = "123456789"
print(s[4])
print(s[-4])
print(s[len(s) - 1])
print(s[-len(s)])

# 15 Find the output.
s = "Programming"
print(len(s))
print(s[10])
print(s[-11])
print(s[11])

"""

String in python : 

A string is a sequence of characters used to represent text. In Python, the built-in str type represents strings.
also string is an Immutable(cannot be changed once it will created) in python. 
Examples include a person's name, email address, city, password text, Pancard Number and a message.

ex : 

name = "Rahul"
city = "Pune"
message = "Welcome to Python"
pancard_number = "FQBPB9467G"

here :

"Rahul" is a string value.
name is a variable referring to that value.
str is the built-in Python data type for strings. 


name = "Rahul"

print(name)
print(type(name))  # output as <class 'str'>


Empty string : 
An empty string contains zero characters.

a = ""
b = ''

this is not consider as empty string :

a = " "
b = "   "


The len() function : 
len() returns the number of characters in a string. 

s = "Rahul"
print(len(s)) # it will provide u result in int like as 5




What is indexing : 

Indexing means accessing an individual character of a string using its position.
Python uses zero-based indexing, which means the first character has index 0.

text = "PYTHON"

print(text[0])
print(text[1])
print(text[3])
print(text[5])

Negative indexing : 
Python also supports negative indexing, which starts from the end of the string. like as -1 

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-6])



Different ways to create strings : 


a = 'Python'
b = "Python"
c = """Python is easy to learn."""
d = '''Python is easy to learn.'''

print(a)
print(b)
print(c)
print(d)


message1 = "I'm learning Python"
message2 = 'He said "Hello"'

used for multiline strings and docstrings. :

message = """Hello students,
Welcome to Python.
Today we are learning strings."""



What is immutability : 
Definition: Immutability means that an object cannot be modified after it has been created.
In Python, strings are immutable. Once a string object is created, its characters cannot be changed in place.



name = "Python"
name[0] = "J"
print(name)


- name[0] accesses the first character, P.
- We try to assign J to that character.
- Python does not allow an individual character in a string to be modified this way.
This is the main idea of string immutability.



Escape Sequence character : 

print("Hello\nWorld")
print("Name:\tAlice")
print("C:\\Users\\Name")
print('It\'s sunny')
print("He said, \"Hello!\"")


"""
