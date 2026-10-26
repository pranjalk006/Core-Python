
# Fibonacci series
series = 10
a = 0
b = 1
i = 0

while i < series :
    print(a)
    c = a+b
    a,b=b,c
    i+=1

    
# reverse of num
n = 63052
rev = 0
digit = 0
while n > 0:
    digit = n % 10 
    rev = rev * 10 + digit
    n= n//10
    print(rev)
    

# Palindrom 
n= 1331
pal = n
rev = 0
while n > 0:
    digit = n % 10 
    rev = rev * 10 + digit
    n= n//10
    print(rev)
if pal == rev:
    print("palindrom")
else:
    print("not palindrom")


# amstrong no.
n=153
temp = n
ams = 0
while n > 0:
    digit = n % 10
    ams = ams + digit**(len(str(n)))
    n = n//10
    print(ams)
if ams == temp:
    print("amstrong no.")
else:
    print("nit amstrong no.")


# Prime no.

num = 3
i = 0
count = 0
while i <= num:
    if num % i == 0:
        count+=1
    i += 1
if count==2:
    print("prime")
else:
    print("not prime")


# Q1 Print numbers from 10 to 1 in reverse order.

i=10
while i>=1:
    print(i,"rev num")
    i-=1


#Q2 Print all even numbers between 1 and 50.

i = 0
while i<=50:
    print(i,"even number")
    i +=2


#Q3 Print all odd numbers between 1 and 50.

i = 1
while i<=50:
    print(i,"odd number")
    i +=2


#Q4 Print the multiplication table of a number entered by the user.

num = int(input("enter number :- "))
table = 0
i = 1
while i<=10:
    table = num * i
    i+=1
    print(table)
   

# Q5 Find the sum of numbers from 1 to n.
n = 5
sum =0
i =0
while i<=n:
    sum=sum + i
    i+=1
print(sum)


#Q6 Find the sum of all even numbers between 1 and n.

n = 10
sum =0
i =0
while i<=n:
    sum=sum + i
    i+=2
print(sum)

#Q7 Print numbers from 1 to 10 using a while loop.
i = 0

while i<=10:
    print(i,"number")
    i+=1

#Q8 Print the squares of numbers from 1 to n.
n = 10
sqr =0
i =0
while i<=n:
    sqr= i ** 2
    i+=1
    print(sqr)


#Q9 Print the cubes of numbers from 1 to n.

n = 10
cube =0
i =0
while i<=n:
   cube = i ** 3
   print("cube of", i, "is", cube)
   i+=1

#Q10 Count how many numbers are between 1 and n.

n=11
i=1
count =0
while i<=11:
   count+=1
  
   i+=1
print(count)


#Q11 Print numbers from 1 to n that are divisible by 5.

n = 20
i=0

while i <=n:
    if i % 5 == 0:
        print(i, "div 5")
    i+=1


# Q12 Calculate the factorial of a number.

n=5
i=1
tempp = 1
while i<=n:
    tempp = tempp * i
    i+=1
print(tempp)

# Q13 Display the first n natural numbers and their sum.

n= int(input("enter no."))
i=1
nat = 0

while i<= n:
    nat += i
    i+=1
    print(nat)

# Q14 Print the multiplication table in reverse order, from 10 to 1.  
table = 0
i = 10
n = 5

while i>= 1:
    table= n * i
    print(table)
    i-=1



# Count the number of digits in a given integer.
n = int(input("enter no."))
count = 0
while n >0:
    count = count + 1
    n = n//10
print("count is",count)


# Find the sum of the digits of a number.

n = int(input("enter no."))
num = 0
sum=0
while n >0:
    num = n % 10
    sum = sum + num
    n = n//10
print("total is ",sum)

# Find the product of the digits of a number.

n = int(input("enter no."))
num = 0
pr=1 
while n >0:
    num = n % 10
    pr = pr * num
    n = n//10
print("total is ",pr)


# Reverse a given number.

n = 285
digit = 0
rev = 0
while n>0:
    digit = n%10
    rev = rev *10 +digit
    n = n//10
print(rev)


    
