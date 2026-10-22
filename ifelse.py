
# A. Simple if Statements
# 1. Write a program to check whether a number is greater than 10.

a = 10
if(a >=10) :
    print("greater than 10")

# 2. Write a program to check whether a person is eligible to vote (age must be 18 or above).

age = int(input("enter age"))
if (age >= 18):
    print("Eligible")
# 3. Write a program to check whether a number is divisible by 5.

num = 50
if(num % 5 == 0):
    print("divisible")

# 4. Write a program to check whether a student has scored at least 35 marks.

mark = 35
if(mark >=35):
    print("scored")

# 5. Write a program to check whether a character is an uppercase letter.
name = "pRANJAL"
if(name.isupper):
    print("all in uppercase")

    

# B. if-else Statements
# 6. Write a program to check whether a number is even or odd.

num1 = int(input("enter number :- "))
if(num1 % 2 == 0) :
    print("number is even")
else :
    print("Number is odd")

# 7. Write a program to check whether a number is positive or non-positive.

num2 = int(input("enter number :- "))
if(num2 >= 0 or num2 == 0):
    print("NUNBER IS POSITIVE")
else:
    print("NUMBER IS NEGATIVE")

# 8. Write a program to check voting eligibility using if-else.

agee = int(input("enter number :- "))
if(agee >= 18):
    print("eligible")
else:
    print("Not eligible ")

# 9. Write a program to check whether a number is divisible by both 3 and 5.

num3 = int(input("enter number :- "))
if(num3 // 3 and num3 // 5) :
    print("divisible by both 3 and 5")
else: 
    print("not divisible by both 3 and 5")

# 10. Write a program to check whether two numbers are equal or different.

num4 = int(input("enter number :- "))
num5 = int(input("enter number :- "))

if(num4 == num5):
    print("equal")
else:
    print("not equal")
    
# 11. Write a program to display Pass if marks are 35 or above; otherwise display Fail.

markk = int(input("enter number :- "))
if(markk >= 35):
    print("pass")
else:
    print("fail")

# 12. Write a program to check whether a year is a leap year.

year = int(input("enter number :- "))

if(year % 400 ==0 or year % 4==0 and year % 100 != 0):
    print("leap year")
else:
    print("not leap")

# D. Nested if Statements
# 21. Write a program to check a username first and then check the password only if the username is correct.

username = "pranjal@06"
password = "pranjal123"

if(username=="pranjal@06"):
    print("correct")
    if(password == "pranjal123")
        print("correct")
    else:
        print("incorrect")

else:
    print("user incorrect")

# 22. Write a program to check whether a person is at least 18 years old and then check whether they are
# registered to vote.

user = int(input("enter number :- "))
register = True

if(user >= 18):
    print("eligible")
    if(register==True):
        print("REGISTERD")
    else:
        print("not register")

else:
    print("not eligible")

# 23. Write a program to check whether a student has passed; if passed, check whether the student has scored at
# least 75 marks for distinction.

markssss = int(input("enter number :- "))

if(markssss>=35):
    print("passes")
    if(markssss>=75):
        print("more then 75")
    else:
        print("no more")
else:
    print("fail")

# 24. Write a program to check whether a number is positive; if positive, check whether it is even or odd.

num = int(input("enter number :- "))

if(num > 0):
    print("positive")
    if(num % 2==0):
        print("even")
    else:
        print("odd")
elif(num==0):
    print("num is zero")
else:
    print("negative")

# 25. Write a program to check whether an applicant meets the minimum age requirement; if so, check whether
# their salary is sufficient for a loan.

a_age = int(input("enter number :- "))
r_age = int(input("enter number :- "))
a_salary = int(input("enter number :- "))
s_sal_loan = int(input("enter number :- "))

if(a_age >= r_age):
    print("done")
    if(a_salary >= s_sal_loan):
        print("sufficient")
    else:
        print("not suf")
else:
    print("not done")

