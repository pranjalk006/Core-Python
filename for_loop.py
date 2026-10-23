# Q1. Print the message 'Welcome to Banking' 5 times.

for i in range (0,5) :
    print("Welcome to Banking")

    
# Q2. Print the numbers from 1 to 10. Consider each number a transaction ID.

for i in range (1,11) :
    print("transaction is -->", i)


# Q3. Print the numbers from 1 to 12, representing the months of a year.

for i in range (1,13):
    print(i,"month of year") 


# Q4. Print the numbers from 10 to 1 in reverse order, representing a countdown before a payment deadline.

for i in range (10,0,-1):
    print("countdown begins", i )


# Q5. Print the numbers 100, 200, 300, ... up to 1000, representing amounts in rupees.

for i in range(100,1100,100):
    print(i,"rs")

# Q6. Print 'Payment Successful' 3 times.

for i in range (1,4,1):
    print("payment successful")


# Q7. Print the numbers from 1 to 7, representing days in a financial week.

for i in range (1,8):
    print(i, "day of week")


# Q8. Print all even numbers from 2 to 20, representing sample transaction amounts.

for i in range (2,21,2):
    print(i,"sample transaction")

   
# Q9. Print all odd numbers from 1 to 19.

for i in range (1,21,2):
    print(i,"odd number")
 
# Q10. Print the numbers from 500 to 1000 in steps of 100.

for i in range (500,1100,100):
    print(i)


# Q11. Print the amount ₹500 five times using a for loop.

for i in range (0,5):
    print("rs 500")


# Q12. Print the numbers from 1 to 5, representing five customers.

for i in range (1,6):
    print(i,"customer")
     
    
# Q13. Print the amounts ₹100, ₹200, ₹300, ₹400, and ₹500 using a for loop.

for i in range (100,600,100):
    print(i,"rs")


# Q14. Print the numbers from 5 to 50 in steps of 5, representing savings milestones.

for i in range (5,55,5):
    print(i, "milestone")

# Q15. Print 'Monthly EMI Due' 12 times.

for i in range(1,12):
    print(i, "emi due")


# Q16. Print the numbers from 1 to 10, representing 10 bank transactions.

for i in range (1,11):
    print(i, "bank transaction")


# Q17. Print the amounts 1000, 900, 800, ... down to 100.

for i in range (1000,0,-100):
    print(i)


# Q18. Print the years 2021 to 2026 using a for loop.

for i in range(2021,2027):
    print(i)
   

# Q19. Print the numbers from 1 to 30 in steps of 3, representing sample reward points.

for i in range(1,31,3):
    print(i)
 

# Q20. Print 'Saving Money Every Day' 7 times.

for i in range (1,8):
    print("saving money")
   

# 21. Print the square of each number from 1 to 10, treating the result as a simple financial calculation exercise.

for i in range (1,11):
    print(i**2)

# 22. Print the cube of each number from 1 to 5.

for i in range (1,6):
    print(i**3)


# 23. Calculate and print the total of the numbers from 1 to 10, representing small daily deposits.

temp = 0
for i in range (1,11):
    temp += i
print('total', temp)
 

# 24. Calculate the total of all even numbers from 2 to 20.

temp1 = 0
for i in range (2,21,2):
    temp1 += i

print(temp1)
    
  
# 25. Calculate the total of all odd numbers from 1 to 19.

temp2 = 0
for i in range (1,20,2):
    temp2 += i
print(temp2)


# 26. Print the amount of money remaining from ₹1,000 after spending ₹100 on each of 5 consecutive days.

money = 1000
for i in range (1,6):
    money -= 100
print(money)

# 27. A person saves ₹500 every month. Print the savings amount for each month over 12 months, assuming savings accumulate without interest.

save = 0
for i in range (1,13):
    save += 500
    print(i, "month", save)


# 28. Calculate the total savings after depositing ₹100, ₹200, ₹300, ... ₹1,000.

cal = 0
for i in range (100,1100,100):
    cal += i
print("calculated money", cal)


# 29. Print the balance after each month if a person starts with ₹5,000 and deposits ₹500 every month for 6 months.

balance = 5000
for i in range (1,7):
    balance += 500
print(i,"month balance", balance)


# 30. Calculate the total amount of 10 monthly deposits of ₹1,000 each.
amt = 0
for i in range (1,11):
    amt +=1000
print(i,"total", amt)

# 31. Print the monthly EMI payment of ₹2,500 for 12 months and calculate the total amount paid. Ignore interest.

emi = 0
for i in range (1,13):
    emi += 2500
    print(i, "months paid", emi)   

# 32. A customer spends ₹200 every day. Print the cumulative spending after each of 7 days.
cus = 0
for i in range (1,8):
    cus += 200
    print(i, "days", cus)


# 33. Calculate the total of transaction amounts ₹100, ₹200, ₹300, ₹400, and ₹500.

total = 0
for i in range (100,600,100):
    total += i
print(total)


# 34. Print the annual salary for each year from 1 to 5 if the starting annual salary is ₹3,00,000 and increases by ₹20,000 every year.

income = 300000
for i in range (1,6):
    income += 20000
    print(i ,"total income", income)

  
# 35. A person has ₹10,000 and withdraws ₹500 every month. Print the remaining balance after each of 10 months.

wd = 10000
for i in range (1,13):
    wd -= 500
    print(i, "remain", wd)


# Level 3: Moderate (36–50)
# Practice totals, repeated calculations, and simple finance-based patterns using only for loops.

# 36. Calculate the total savings if a person deposits ₹100 on day 1, ₹200 on day 2, and continues increasing the daily deposit by ₹100 for 10 days.

savings = 0
for i in range (1,11):
    deposit = i * 100
    savings = savings + deposit
    print(i, "day savingd total", savings)
  

# 37. Print the multiplication table of ₹500 from 1 to 10, showing multiples as savings targets.

table = 500
for i in range (1,11):
    table = 500 * i
    print(i, "into 500", table)



# 38. Calculate the total amount paid over 12 months if monthly rent starts at ₹5,000 and increases by ₹200 every month.

totall = 0
rent = 5000

for i in range (1,13):
    rent += 200
    totall = totall+rent
    print(i, "month total is", totall)


# 39. A person invests ₹1,000 every month for 12 months. Print the cumulative invested amount after each month, ignoring returns.
invest = 0

for i in range (1,13):
    invest += 1000
    print(i, "month total invest", invest)
 


# 40. Calculate the total of all transaction amounts from ₹500 to ₹5,000 in increments of ₹500.

inamt = 0
for i in range (500,5001,500):
    inamt = inamt+1
    print(i,"incremented amt", inamt)


# 41. Print the balance for 12 months if the initial balance is ₹20,000 and ₹1,000 is withdrawn every month.

balance =  20000

for i in range (1,13):
    balance -= 1000
    print(i, "month withdrwal money", balance)



# 42. Calculate the total simple interest on ₹10,000 at an annual interest rate of 5% for each duration from 1 to 5 years. Use the formula \(SI = \frac{P \times R \times T}{100}\).

principal  = 10000
rate = 5

for i in range(1, 6):
    si = (principal*rate*i) / 100
    print( i," year simple interest:", si)

    

# 43. Print the total balance for each year from 1 to 5 if ₹10,000 earns simple interest at 5% annually, with no additional deposits or withdrawals.

p = 10000
r = 5
total = 0
for i in range (1,6):
    si = (p*r*i) /100
    total= p + si
    print(i,"total is", total)

  

# 44. A person saves ₹1,000 in the first month and increases their monthly deposit by ₹500 each month. Calculate the total savings over 6 months.

saves = 1000
deposit = 500

for i in range (1,7):
    saves += deposit
    print(i,"month balance", saves)
  

# 45. Print the yearly salary for 5 years if the first year's salary is ₹4,00,000 and it increases by 10% of the original salary each year.


# Q46. Daily Expenses
# A person spends ₹150 on the first day and increases daily expenses by ₹50 for 7 days. Calculate total expenses.

spent = 150
total = 0
for i in range(1, 8):
    total = total + expense
    expense = expense + 50

print("Total expenses:", total)


# Q47 A household pays ₹700 in the first month, and the bill increases by ₹50 each month. Print each month's bill and calculate the total for 12 months.
total = 0
bill = 700
for i in range(1, 13):
    total = total + bill
    bill = bill + 50

print("Total electricity bill:", total)


#Q48 loan eligibility

for age in range(18, 31):
    if age >= 21:
        print("Eligible")
    else:
        print("Not Eligible")

# Q49 Profit or looss

for i in range(0, 6):
    if i > 0:
        print(i, "Profit")
    elif i < 0:
        print(i, "Loss")
    else:
        print(i, "No Profit No Loss")

# Q50 num is +ve or -ve

for i in range(-5, 6):
    if i > 0:
        print(i, "Positive")
    elif i < 0:
        print(i, "Negative")
    else:
        print(i, "Zero")
