# 1 Even Odd
#1.1 args with return type
def evenodd(a):
    if a % 2==0:
       return "even"
    else:
        return "odd"

# print(evenodd(5))


# 1.2 args without return type
def evenodd(a):
    
    if a % 2==0:
        print("even")
    else:
        print("odd")

# evenodd(6)


# 1.3  no args with return type
def evenodd():
    a = 6
    if a % 2==0:
       return "even"
    else:
        return "odd"

# print(evenodd())

# 1.4 no args without return type
def evenodd():
    a = 6
    if a % 2==0:
      print("even")
    else:
        print("odd")

# evenodd()

# 2 +ve and -ve
# 2.1 #1.1 args with return type
def posneg (b):
   if b > 0:
       return "positive"
   else:
       return "negative"

# print(posneg(-3))

# 2.2 args without return type
def posneg (b):
   if b > 0:
       print("positive")
   else:
       print("negative")

# n= posneg(5)
# print(n)

# 2.3 no args with return type
def posneg():
   b = int(input("enter number"))
   if b > 0:
       return "positive"
   else:
       return "negative"
# print(posneg())

# 2.4 no args without return type
def posneg ():
   b= int(input("enter number"))
   if b > 0:
       print("positive")
   else:
       print("negative")
# posneg()

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
# print(rev(345))

# 3.2 args without return type
def rev(r):
    digit=0
    rev=0
    while r >0:
        digit = r % 10
        rev = rev * 10 + digit
        r = r//10
    print(rev)
# rev(345)

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
# print(rev())

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
# rev()

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
# print(pall(313))

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
# pall(121)/

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
# print(pall())

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
# pall()

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

# print(primee(7))

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
# primee(34569)

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
# print(primee())

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

# primee()