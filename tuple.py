# Practise questions
#1. Create a tuple containing five integers and print it.

a = (34,567,234,8,4,45)
print(a)
# 2. Create a tuple containing a string, integer, float, and Boolean value.

b = 23,"xyz",23.45,True,345
print(b)
print(type(b))

# 3. Create a single-element tuple and verify its datatype.

c= (45,)
print(type(c))

# 4. Print the first, middle, and last elements of a tuple.
d = ("pranjal", "U", "K")
name, midname, lastname = d
print(name,midname,lastname)

# 5. Reverse a tuple using slicing.
e = (34,56,78,32,4,8,31,67)
print(e[::-1])

# 6. Print every second element using slicing.
e = (34,56,78,32,4,8,31,67)
print(e[::2])

# 7. Count how many times 25 occurs in a tuple.

f = 34,45,25,25,7,6,2,25,25,67,25,47,25
print(f.count(25))

# 8. Find the index of a given element.

f = 34,45,25,25,7,6,2,25,25,67,25,47,25
print(f.index(45))

# 9. Calculate the sum and average of numeric tuple elements.

g = 2,4,6,8,10
total = 0
print(sum(g))
print(sum(g) / len(g))

# 10. Count even and odd numbers in a tuple.

h = 1,2,23,4,6,79,8,10
e_count = 0
o_count=0
for i in h:
    if (i % 2 == 0):
        e_count+=1

o_count= len(h) - e_count
print(e_count)
print(o_count)

# 11. Find the maximum and minimum values.

i = (34,56,78,32,4,8,31,67)
print(min(i))
print(max(i))

# 12. Check whether a particular value exists in a tuple.

j=(34,56,78,32,4,8,31,67)
print(24 in j)
print(78 in j)

# 13. Convert a list into a tuple.

k= [4,675,345,678]
t1 = tuple(k)
print(t1)
print(type(t1))

# 14. Unpack a tuple into four variables.
l = "pranjal", "python", 20, "pune"
name, course, age, city = l
print(name, course, age, city)

# 15. Swap two variables using tuple unpacking.
m= "pranjal", "python"
name, course = m
nav , kam = name, course
print(nav, kam)

# 16. Access a specific value from a nested tuple.

n = (("a",1), ("b",2), ("c",3))
print(n[2])
print(n[1][1])
# 17. Remove duplicate values while preserving order.

o = (1,1,2,3,4,5,2,5,6)
pre = []

for i in o:
    if i not in pre:
        pre.append(i)

l1 = tuple(pre)
print(pre)


# 18. Find the second-largest distinct number.

p = (34,56,78,32,4,8,31,67)
t = list(p)
t.sort()
print(t)
p= tuple(t)

print(t[-2])

# 19. Sort a tuple in ascending order and convert the result back into a tuple.

q = (34,56,78,32,4,8,31,67)
l2 = list(q)
l2.sort()
q =tuple(l2)

print(q)

# 20. Create a tuple of student names and marks, then print each student's details.

std = (("rahul", 50), ("priya",90),("ram",60),("sneha", 95))
for name, marks in std:
    print(name, marks)

