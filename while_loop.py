
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



    
