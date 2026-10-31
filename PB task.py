"""
#  even or odd

num= int(input("enter num "))
if num % 2==0:
    print("even")
else:
    print("odd")

# +ve and -ve

num1 = int(input("enter num "))
if num > 0:
    print("positive")
else:
    print("negative")

# rev using for

n = 12345
rev = 0
digit = 0
while n > 0:
    digit = n % 10 
    rev = rev * 10 + digit
    n= n//10
    print(rev)


    
# pallinndrome
num3 =1221
pal= n
rev =0
digit=0
while n> 0:
    digit= num3 % 10
    rev = rev *10 + digit
    num3= num3 // 10
    print(rev)

if rev == pal:
    print("true")
else:
    print("false")

# prime

num4 = 2
cnt = 0

for i in range(1,num4+1):
    if num4 % i ==0:
        cnt+=1

if cnt ==2:
    print("prime")
else:
    print("not prime")

# 1 to 100

# factorial

num5 = 5
temp = 1
i=1
while i<= num5:
    temp = temp * i
    print(temp)
    i+=1

# 
num6 = 2
print(num6**2)
print(num6**3)



#  list
# eve odd

l1=[2,3,4,5,6,7,8,9]
e_count = 0
o_count =0

for i in l1:
    if i % 2 ==0:
        e_count+=1
    else:
        o_count+=1
print(e_count)
print(o_count)

# 
l1=[2,3,4,5,6,7,8,9]
e2 =[]
o2=[]
for i in l1:
    if i % 2 ==0:
        e2.append(i)
    else:
        o2.append(i)
print(e2)
print(o2)


# pre
l1=[2,3,4,5,6,7,8,9]
for i in l1[::-1]:
    print(i)
  

# prime

l2=[2,3,4,5,6,7,8,9]

for i in l2:
    count=0
    for j in range(1,i+1):
        if i % j ==0:
            count+=1

    if count==2:
     print(i)
    

# string

l3=[32,"xyz",65,"pqr"]
for i in l3:
    if i==str(i):
        print(i)

l3=[32,"xyz",65,"pqr"]
for i in l3:
    if i!=str(i):
        print(i)
 

# tuples

t1 = 2,4,6,8,10,12
count = 0
print(max(t1))
print(min(t1))
print(sum(t1))

for i in t1:
    count+=1
print(count)
 

# 
t2 = 2,4,5,6,7,8,10,12
cnt = 0
for i in t2:
    if i %2==0:
        print(i)
       

# Dict 

a = {"name": "pranjal", "age": 20, "city":"pune"}
print(a)
 

# 
b ={"a":50,"b":60,"c":70}
total=0
for m in b.values():
    total = total+ m
print(total)

# 
b ={"a":50,"b":60,"c":70}
for name, marks in b.items():
    if marks > 55:
        print(name, marks)

# 

b ={"a":50,"b":60,"c":70}
highest = 0

for marks in b.values():
    if marks > highest:
        highest=marks
print(highest)
 """

a = "abcd"
b = "".join(reversed(a))
print(b)
