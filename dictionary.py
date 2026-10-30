
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
