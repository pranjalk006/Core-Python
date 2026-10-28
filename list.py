numbers = [4,5,5,1,7,1,8,4, "xyz", True,56.65]

print(numbers,"list ")

# +ve and -ve indexing
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[-1])
print(numbers[-2])
# updating values
numbers[1]=200
numbers[2]=100

# adding elements
numbers.insert(0,600)
print(numbers)

numbers.append(700) # add at last
numbers.append([54,65,2,5])

numbers.extend(567)
numbers.extend([7,6,3,7,3,]) # it wil add 1-1 values(iterate)

numbers.remove(700)


m=numbers.copy()
print(m==numbers) # checks value is same oe not
print(m is numbers) # checks object same or not

marks = [75,5,34,7,24,97]

total = sum(marks)
print(total)
avg = total / len(marks)
print(avg)


num = [34,65,87,29,34]

for y in range (len(num)):
    print(num[y])

for i in num:
    print(i)




i=0
while i<= len(num):
    print(num[i])
    i+=1




n = [34,56,35,87,34,58]
print(n [1:5])
print(n [::-1])
print(n [3:])


a= [23,56,35,53,90,89]
b= [98,34,86,34,75,24]
print(a+b)



# practice questions
# 1
x= [23,7,"pqr",32.14,True]
for i in x:
    print(i)

# 2
y = [2,4,6,8,10]
sum=0
for j in y:
    sum= sum+j
print(sum)


# 3
z = [45,55,25]
if z[0]>z[1] and z[0] > z[2]:
    print(z[0], "is greater")
elif z[1]>z[2] and z[1] > z[0]:
    print(z[1]," is greater")
else:
    print(z[2], "is greater")


# 4
p = [34,5,88,26,70]
e_count = 0
o_count = 0
for i in p:
    if i % 2==0:
        e_count+=1
    else:
        o_count +=1
        
print("even", e_count)
print("odd", o_count)


