# Arithmetic operators

# Calculate the total price of 5 notebooks if one notebook costs â‚¹40

price = 40
notebooks = 5
total_price = price*notebooks
print(" total price is", total_price)

# Calculate the remaining balance after spending â‚¹350 from â‚¹1,000.

balance = 1000
spent = 350
remaining_balance = balance-spent
print("remaining balance is", remaining_balance)

#Calculate the area of a rectangle with length 15 and width 8.

length = 15
width = 8
area_rectangle = length*width
print("Area of rectangle is", area_rectangle)

# Divide 57 chocolates equally among 6 students and display the quotient and remainder.

chocolate = 57
student = 6
print("divided equally", chocolate // student )
print("The quotient is", chocolate / student)
print("The Remainder id", chocolate % student)

# Calculate the square and cube of a number.

num = 6
square = num ** 2
cube = num ** 3

print("Square is", square)
print("cube is", cube)

#Convert a total number of minutes, such as 135, into hours and remaining minutes using // and %.

minutes = 135
hours = minutes // 60
remaining_min = minutes % 60

print("total hours", hours)
print("remaining min", remaining_min)

# Calculate the average of three numbers using arithmetic operators.

a , b, c = 10,20,30
avg = (a+b+c)/3
print("Average is", avg)


# Logical and Comparision operators

print (not (True) and 31 >= 34 or not(32> (True)) and not (True or 56 != 0))

print (not(0 == 0) and 34 >= 34 or not(32 and not (False)) and not (False or 0 != 0))

print(("Ram" == "ram") and (e> 0) and 34 != 34 or not(32 >= 21 and not(True)) and not(True or 56 != e))

print (not (False) and 34 != 34 or not(int("32") >= 21 and not (True)) and not(True or 0.1 != 0))

print (not (False) and 34 <= 0 or not(32 >= 21 and not( '''Sahil''' == 'Sahil''')) and not (True or 56 != 0))


# Comparision Opertors

aa = int(input("Enter a number"))
bb = int(input("Enter a number"))

print(aa >= bb)

c = int(input("Enter a number"))
print(c > 18)

d = int(input("Enter a number"))
e = int(input("Enter a number"))
print(d != e)

student = 50
print(student>=40)

b = int(input("Enter a number"))
a = int(input("Enter a number"))

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


# Logical Operators

a= 10
b = 20
print(a > b and a > 15 )
print(a < b and a > 15 )
print( not(a > b) )

age= 25
print(age >=18 and age<=60)

marks = 35
print(marks >= 40 or marks== 35)

age1 = int(input("enter age -"))
salary = int(input("enter salary -"))
print(age1 >= 18 and salary >=20000)

first = int(input("Enter a number"))
second = int(input("Enter a number"))
print(first > 10)
print(second > 10)



# ref code : 


a = 34
b = "10"

print(a+int(b))


a = int(input('Enter First No --> '))  # 9
b = int(input('Enter 2nd No --> '))   # 2

print("Addition of",a," + ",b," --> ",a+b)
print("Sub of",a," - ",b," --> ",a-b)
print("Mul of",a," * ",b," --> ",a*b)
print("Div of",a," / ",b," --> ",a/b)  
print("Mod of",a," % ",b," --> ",a%b) 
print("Floor Div of",a," // ",b," --> ",a//b)  
print("Exponential of",a," ** ",b," --> ",a**b) 



#  Comparison 

a = 45
b = 4

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >=  b)
print(a <= b)


age = 18 

if(age >= 18):
    print("U R eligible for voting ")
else:
    print("Not Eligible for voting ")  

marks = 80
print(marks > 50)  


print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)


print(not(True and True))


print(22 == 22 and 41 != 23 and (45 == 54))
print(True and True and False)

print(not(True) and not(45 > 566 and 566 == 566))

print(not(False) and 34 != 34 or not(32 >= 21 and not(True)))
print(True and False or True)


# assignment operator
x = 20
x //= 3
x += 7
print(x)

x = 5
x **= 3
x %= 10
print(x)


# Membership operator

x = "Python"
print("P" in x)
print("p" in x)


numbers = [10, 20, 30, 40]
print(20 in numbers)
print(50 not in numbers)

# SECTION A: ARITHMETIC OPERATORS (+, -, *, /, //, %, **)

# Q1
a = 15 // 4
b = 15 % 4
print(a, b)

# Q02
x = -15 // 4
y = -15 % 4
print(x, y)

# Q03
res = 2 ** 3 ** 2
print(res)

# Q04
p = 10 + 3 * 2 ** 2 - 4 / 2
print(p)

# Q05
val = 10.0 % 3
print(type(val), val)

# Q06
a = 7
b = 2.0
print(a // b)

# Q07
x = 5.5 + 4.5 * 2 // 3
print(x)

#SECTION B: RELATIONAL / COMPARISON OPERATORS (==, !=, >, <, >=, <=)

# Q08
print(10 == 10.0)

# Q09
print("apple" > "Apple")

# Q10
print([1, 2] < [1, 2, 0])

# Q11
print(True == 1, False == 0)

# Q12
a = 5
print(1 < a < 10)

# Q13
print(10 != 10.0)

# SECTION C: LOGICAL OPERATORS (AND, OR, NOT)

# Q14
x = 0 and 10
y = 5 and 20
print(x, y)

# Q15
a = "Hello" or ""
b = "" or "World"
print(a, b)

# Q16
print(not [] and not "0")

# Q17
res = 10 or 1 / 0
print(res)

# Q18
x = [] or [0] or False
print(x)

# Q19
print(not (5 > 2 and 3 < 1))

# Q20
a = True
b = False
print(a and not b or b)

# SECTION D: ASSIGNMENT & COMPOUND OPERATORS (=, +=, -=, *=, /=, %=, //=, **=, :=)

# Q21
a = 10
a += 5 * 2
print(a)

# Q22
x = 8
x //= 3
print(x)

# Q23
lst = [1, 2]
lst += [3, 4]
print(lst)

# Q24
a = 5
a **= 2
print(a)

# Q25
if (n := len("Python")) > 5:
 print(n)

# Q26
x = 12
x %= 5
print(x)

#SECTION E: BITWISE OPERATORS (&, |, ^, ~, <<, >>)

# Q27
a = 5 # 0101
b = 3 # 0011
print(a & b, a | b)

# Q28
a = 5 # 0101
b = 3 # 0011
print(a ^ b)

# Q29
x = 10
print(~x)

# Q30
print(~(-5))

# Q31
x = 3 # 0011
print(x << 2)

# Q32
x = 16 # 10000
print(x >> 3)

# Q33
a = 1
print((a << 3) - 1)

#SECTION F: MEMBERSHIP OPERATORS (IN, NOT IN)

# Q34
s = "py" in "python"
print(s)

# Q35
d = {"a": 1, "b": 2}
print(1 in d, "a" in d)

# Q36
print(1 not in [1, 2, 3])

# Q37
t = (1, [2, 3])
print(2 in t)

# Q38
print("th" not in "python")

# Q39
st = {1, 2, 3}
print(3 in st)

# Q40
a = [1, 2]
b = [1, 2]
print(a is b, a == b)

# SECTION G: IDENTITY OPERATORS (IS, IS NOT)

# Q41
x = 256
y = 256
print(x is y)

# Q42
m = "hello"
n = "hello"
print(m is n)

# Q43
a = None
print(a is None)

# Q44
p = [10]
q = p
print(p is not q)

# Q45
x = True
y = 1
print(x is y)

# SECTION H: COMBINED & SPECIAL OPERATOR PRECEDENCE CHALLENGES

# Q46
a = 10
b = 20
c = 30
print(a < b and b < c or a > c)

# Q47
x = 5
print(x & 1 == 0)

# Q48
a = [1, 2]
b = a
b += [3]
print(a is b, a)

# Q49
a = [1, 2]
b = a
b = b + [3]
print(a is b, a)

# Q50
x = 10
y = 5
z = x > y and x & y or x ^ y
print(z)

# Membership Operator

# Q1 Create a string: language = "Python" Check whether "P" exists in the string.
language = "Python"
print("P" in language)

#Q2 Check whether "Java" exists in: courses = ["Python", "Java", "SQL"]
courses = ["Python", "Java", "SQL"]
print("Java" in courses)

# Q3 Check whether "C++" does not exist in the above list.
print("c++" in courses)

#Q4 Take a name from the user and check whether "a" exists in the name.
name = input("enter name  ")
print("a" in name)

#Q5 Take an email from the user and check whether "@" exists in it.
email = input("enter email  ")
print("@" in email)

#Q6 Create: numbers = [10, 20, 30, 40, 50] Check whether 30 and 100 are present.
numbers = [10, 20, 30, 40, 50]
print("30" and "100" in numbers)

#Q7 Create: languages = ["Java", "Python", "C", "C++"] Check whether "Python" is present and "Ruby" is not present.
languages = ["Java", "Python", "C", "C++"]
print("python" in languages)


#Identity Operator : 

a = 10
b = 20

c = 30
d = 30

e = 50
f = e

print(a is b)
print(c is d)
print(e is f)


