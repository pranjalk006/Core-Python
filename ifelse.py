
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
   

