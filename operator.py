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

