
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


    
