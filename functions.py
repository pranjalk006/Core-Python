# 1 Even Odd
#1.1 args with return type
def evenodd(a):
    if a % 2==0:
       return "even"
    else:
        return "odd"

print(evenodd(5))


# 1.2 args without return type
def evenodd(a):
    
    if a % 2==0:
        print("even")
    else:
        print("odd")

evenodd(6)


# 1.3  no args with return type
def evenodd():
    a = 6
    if a % 2==0:
       return "even"
    else:
        return "odd"

print(evenodd())

# 1.4 no args without return type
def evenodd():
    a = 6
    if a % 2==0:
      print("even")
    else:
        print("odd")

evenodd()

# 2 +ve and -ve
# 2.1 #1.1 args with return type
def posneg (b):
   if b > 0:
       return "positive"
   else:
       return "negative"

print(posneg(-3))

# 2.2 args without return type
def posneg (b):
   if b > 0:
       print("positive")
   else:
       print("negative")

n= posneg(5)
print(n)

# 2.3 no args with return type
def posneg():
   b = int(input("enter number"))
   if b > 0:
       return "positive"
   else:
       return "negative"
print(posneg())

# 2.4 no args without return type
def posneg ():
   b= int(input("enter number"))
   if b > 0:
       print("positive")
   else:
       print("negative")
posneg()

# 3 rev no.
# 3.1 args with return type
def rev(r):
    digit=0
    rev=0
    while r >0:
        digit = r % 10
        rev = rev * 10 + digit
        r = r//10
    print(rev)
    return rev
print(rev(345))

# 3.2 args without return type
def rev(r):
    digit=0
    rev=0
    while r >0:
        digit = r % 10
        rev = rev * 10 + digit
        r = r//10
    print(rev)
rev(345)

# 3.3 no args with return type
def rev():
    r=859
    digit=0
    rev=0
    while r >0:
        digit = r % 10
        rev = rev * 10 + digit
        r = r//10
    return rev
print(rev())

# 3.4 no args without return type
def rev():
    r=348
    digit=0
    rev=0
    while r >0:
        digit = r % 10
        rev = rev * 10 + digit
        r = r//10
    print(rev)
rev()

#  4 Pallindrome
# 4.1 args and return type
def pall(p):
    pal = p
    rev = 0
    for i in range (len(str(p))):
        digit = p %10
        rev = rev * 10 +digit
        p= p // 10
    if pal ==rev:
        return "palindrome"
    else:
        return"not palindrome"
print(pall(313))

# 4.2 args without return type
def pall(p):
    pal = p
    rev = 0
    for i in range (len(str(p))):
        digit = p %10
        rev = rev * 10 +digit
        p= p // 10
    if pal ==rev:
       print( "palindrome")
    else:
        print("not palindrome")
pall(121)/

# 4.3 no args with returntype
def pall():
    p= 456
    pal = p
    rev = 0
    for i in range (len(str(p))):
        digit = p %10
        rev = rev * 10 +digit
        p= p // 10
    if pal ==rev:
        return "palindrome"
    else:
        return"not palindrome"
print(pall())

# 4.4 no args without return type
def pall():
    p= 34567
    pal = p
    rev = 0
    for i in range (len(str(p))):
        digit = p %10
        rev = rev * 10 +digit
        p= p // 10
    if pal ==rev:
        print("palindrome")
    else:
        print("not palindrome")
pall()

# 5 prime no.
# 5.1 
def primee(c):
    count = 0
    for i in range (1,c+1):
        if c % i ==0:
            count+=1

    if count==2:
        return "prime"
    else:
        return"not prime"

print(primee(7))

# 5.2
def primee(c):
    count = 0
    for i in range (1,c+1):
        if c % i ==0:
            count+=1

    if count==2:
        print("prime")
    else:
        print("not prime")
primee(34569)

# 5.3
def primee():
    c = 2343
    count = 0
    for i in range (1,c+1):
        if c % i ==0:
            count+=1

    if count==2:
        return "prime"
    else:
        return"not prime"
print(primee())

# 5.4
def primee():
    c= 874
    count = 0
    for i in range (1,c+1):
        if c % i ==0:
            count+=1

    if count==2:
        print("prime")
    else:
        print("not prime")

primee()

# 6 Amstrong
# 6.1 args with return type
def amsno(num):
    temp = num
    ams = 0
    for i in range (len(str(num))):
        digit = num % 10
        ams = ams + digit**(len(str(temp)))
        num= num//10
        print(ams)

    if temp == ams:
        return "amstrong"
    else:
        return"not ams"
print(amsno(153))

# 6.2 args without return type
def amsno(num):
    temp = num
    ams = 0
    for i in range (len(str(num))):
        digit = num % 10
        ams = ams + digit**(len(str(temp)))
        num= num//10
        print(ams)

    if temp == ams:
        print("amstrong")
    else:
        print("not ams")
amsno(345)

# 6.3 no args with return type
def amsno():
    num = 23456
    temp = num
    ams = 0
    for i in range (len(str(num))):
        digit = num % 10
        ams = ams + digit**(len(str(temp)))
        num= num//10
        print(ams)

    if temp == ams:
        return "amstrong"
    else:
        return"not ams"
print(amsno())

# 6.4 args without return type
def amsno():
    num=153
    temp = num
    ams = 0
    for i in range (len(str(num))):
        digit = num % 10
        ams = ams + digit**(len(str(temp)))
        num= num//10
        print(ams)

    if temp == ams:
        print("amstrong")
    else:
        print("not ams")
amsno()

# 7 voting
# 7.1 args with return type
def vote(user):
    if(user >= 18):
        return"eligible"
    else:
        return "not eligible"
user = int(input("enter number :- "))
print(vote(user))

# 7.2 args without return type
def vote(user):
    if(user >= 18):
        print("eligible")
    else:
        print("not eligible")
user = int(input("enter number :- "))
vote(user)

# # 7.3 no args with return type
def vote():
    user = int(input("enter number :- "))
    if(user >= 18):
        return"eligible"
    else:
        return "not eligible"
print(vote())

# 7.2 no args without return type
def vote():
    user = int(input("enter number :- "))
    if(user >= 18):
        print("eligible")
    else:
        print("not eligible")
vote()

# 8 div 3 and 5
# 8.1 args without return type
def div_3_5(no1):
    if(no1 // 3 and no1 // 5) :
        print("divisible by both 3 and 5")
    else: 
        print("not divisible by both 3 and 5")
div_3_5(65)

# 8.2 args with return type
def div_3_5(no1):
    if(no1 // 3 and no1 // 5) :
       return "divisible by both 3 and 5"
    else: 
        return "not divisible by both 3 and 5"
print(div_3_5(65))


# 8.3 no args with return type
def div_3_5():
    no1 = 567
    if(no1 // 3 and no1 // 5) :
       return "divisible by both 3 and 5"
    else: 
        return "not divisible by both 3 and 5"
print(div_3_5())

# 8.4 args without return type
def div_3_5():
    no1 = 34
    if(no1 // 3 and no1 // 5) :
        print("divisible by both 3 and 5")
    else: 
        print("not divisible by both 3 and 5")
div_3_5()


# 9 equal or not
# 9.1 
def eql(x,y):
    if(x == y):
        return "equal"
    else:
        return "not equal"
x = int(input("enter number :- "))
y = int(input("enter number :- "))
print(eql(x,y))

# 9.2
def eql(x,y):
    if(x == y):
        print("equal")
    else:
        print ("not equal")
x = int(input("enter number :- "))
y = int(input("enter number :- "))
(eql(x,y))

# 9.3
def eql():
    x = int(input("enter number :- "))
    y = int(input("enter number :- "))
    if(x == y):
        return "equal"
    else:
        return "not equal"

print(eql(x,y))

# 9.4
def eql():
    x = int(input("enter number :- "))
    y = int(input("enter number :- "))
    if(x == y):
        print("equal")
    else:
        print ("not equal")

(eql(x,y))


# 10 multipl
# 10.1
def multi(empid, ename, dept):
    return empid, ename, dept
print(multi(10,"pranjal","comp"))

# 10.2
def multi(empid, ename, dept):
    print(empid, ename, dept)
multi(10,"pranjal","comp")

# 10.3
def multi():
    empid, ename, dept = 10,"pranjal","comp"
    return empid, ename, dept
print(multi())

# 10.4
def multi():
    empid, ename, dept = 10,"pranjal","comp"
    print(empid, ename, dept)
multi()



# Positinoal args , V L keyword args, default value, nested def

#1  Write a function calculate_area(length, breadth) that returns the area of a rectangle. Take both values from the user and display the result

def rect(*args):
    area=1
    for n in args:
        area*=n
    print(area)
rect(10,20)
    multi()

#2.  Write a function simple_interest(principal, rate, time) that returns the simple interest. Call it with positional arguments for two different sets of values.

def simple_interest(*args):
    si = 1
    for num in args:
        si*=num
        si/100
    print(si)

simple_interest(1000,2,3)
      

# 3. Write a function student_info(name, branch, year) that prints a formatted line. Call it using keyword arguments in a different order than defined.

def student_info(**kwargs):
    print(kwargs)
student_info(name="xyz", branch = "comp", year= 2018)


# Write a function create_profile(name, age, city) and call it by mixing one positional argument with two keyword arguments.

def create_profile(**kwargs):
    for i,j in kwargs.items():
     print(i,":",j)

create_profile(name="xyz", age = 20, city="pune")  


# 5. Write a function power(base, exponent=2) that returns base ** exponent. Call it with only the base, with both values positionally, and with the exponent as a keyword argument.
def power(base, exponent=2):
    print(base**exponent)

power(2)
power(2,3)


# 6. Declare a global variable x = 50. Write a function that creates a local variable x = 10 and prints it. Print x outside the function and show that the global value is unchanged.
x=50
def globallocal():
    x=10
    print(x)

print(x)
globallocal()

# 7. Write a program with a global variable counter = 0 and a function increment() that uses the global keyword to increase it by 1. Call it five times and print the final value.
counter = 0
def increment():
    global counter 
    counter +=1

increment()
increment()
increment()
increment()
increment()
print("final", counter)


# 8. Write a program with a global list marks = [70, 80]. Write a function that appends a new mark to it *without* using the global keyword. Print the list and explain in a comment why this works.

marks = [70,80]
def lmark():
    marks.append(10)
lmark()
print(marks)


# 9. Write a function outer(a, b) that defines an inner function inner() returning a + b. Call inner() inside outer() and print the result.
def outer(a,b):
    def inner():
        return a+b
    print("addition ",inner())
outer(10,20)
