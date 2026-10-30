
# 1. Create a dictionary containing your name, age, and city.

details = {"name": "pranjal", "age": 20, "city":"pune"}
print(details)

# 2. Print only the name from a student dictionary.
std  = {"name":"xyz", "course":"python", "age":20}
print(std["name"])

# 3. Add an email key to an existing dictionary.
std  = {"name":"xyz", "course":"python", "age":20}
std["email"] = "xyz@gmail.com"
print(std)

# 4. Update an employee's salary.
emp = {"name": "pranjal", "age": 20, "city":"pune", "salary": 100000}
emp ["salary"]= 300000
print(emp)

# 5. Remove the age key from a dictionary.
a= {"name": "pranjal", "age": 20, "city":"pune"}
a.pop("age")
print(a)

# 6. Print all keys and values using a for loop.
emp = {"name": "pranjal", "age": 20, "city":"pune", "salary": 100000}
for i in emp.items():
    print(i)
    
# 7. Check whether the key 'course' exists.

std  = {"name":"xyz", "course":"python", "age":20}
print("course" in std)

# 8. Count the number of key-value pairs.

emp = {"name": "pranjal", "age": 20, "city":"pune", "salary": 100000}
print(len(emp))

# 9. Create a nested dictionary for three students.

n_dict= {1:{"name":"pranjal", "marks":100},2:{"name":"Anushka","marks":90}}
print(n_dict)

# 10. Create a dictionary of numbers and their squares from 1 to 10.

s_dict = {number : number **2 for number in range(1,10)}
print(s_dict)

# 11. Print only students who scored more than 75.
students = {"a": 80, "b": 65, "c": 90,"d": 72,"e": 85}

for name, marks in students.items():
    if marks > 75:
        print(name, marks)

  
# 12. Count the frequency of each character in a string using a dictionary.

a= {"name": "pranjal", "age": 20, "city":"pune"}
data = list(a.items())
for i in range(len(data)):
    print(data[i])
# 13. Use range() to print dictionary entries by position after converting items to a list.


# 14. Use fromkeys() to initialize five subject marks to zero.
subjects = ["Python", "Java", "SQL", "HTML", "CSS"]
marks = dict.fromkeys(subjects,100)
print(marks)
  
# 15. Copy a dictionary and demonstrate that changing a top-level value in the copy does not change
# the original.

a = {"name": "pranjal", "age": 20, "city":"pune"}
b= a.copy()
b["age"]=21

print(a)
print(b)
