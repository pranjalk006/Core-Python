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


