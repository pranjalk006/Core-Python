# Q1 Quarter 

month = "dec"

match month.capitalize() :
    case "Jan"|"Feb"|"Mar"|"Apr" :
        print("first Quarter")

    case "May"|"June"|"July"|"Aug" :
        print("Seconf Quarter")

    case "Sep"|"Oct"|"Nov"|"Dec" :
        print("Third quarter")

    case _:
        print("invalid")

#Q2 Grade

marks = 50
match marks :
    case a if marks <= 35 and marks < 0:
        print("c grade")

    case b if marks < 70 and marks> 35:
        print("b grade")

    case c if marks < 100 and marks > 70:
        print("a grade")

    case _ :
        print("fail")

# Q3 Power of
ch = 2
num = 5

match ch :
    case 1 :
        print("sqr", num**2)

    case 2 :
        print("cube", num**3)

    case 3 :
        print("power 4", num**4)

    case _ :
        print("invalid")

# Q4 vowels

temp = "icecreaaam"
ch = "a"
match ch:
    case "a"|"e"|"i"|"o"|"u":
        print(temp.count(ch))

    case _ :
        print("invalid")

# Q5. Simple Calculator

num1 = int(input("enter number "))
num2 = int(input("enter number "))
choice = (input("enter opration "))

match choice :
    case "addition" :
        print(num1+num2)

    case "subtraction":
        print(num1 - num2)

    case "multiplication":
        print(num1 * num2)

    case "Division":
        print(num1 / num2)

    case _:
        print("invalid opration")
      

# Q6 Pizza Size: Take S, M, or L and print Small, Medium, or Large.

size = input("enter size")
chh = "s"

match chh :
    case "s"|"m"|"l":
        print("size is", chh)

    case _ :
        print("invlid size")



#Q7 ATM System

balance = 500000
withdraw= 0
deposit = 0

choice = int(input("1. Check Balance \n 2. Withdraw \n 3. Deposit \n 4. Exit \n Enter ur choice...!"))

match choice:
    case 1:
        print(f"Your Balance is ,{balance}")
    case 2:
       withdraw = int(input("Enter amount to withdraw..."))
       print(f"Withdrawal Amount {withdraw}\n Updated balance is",balance-withdraw) 
    case 3:
        deposit = int(input("Enter amount to deposit"))
        print(f"Deposited amount {deposit}\n Updated balance is",balance-withdraw)
    case 4:
        print("U r exited.")
    case _:
        print("Invalid Input")

        

# Q8 Mobile Brand

xyz = int(input("enter name "))

match xyz :
     case 1 :
        print("Oneplus")

     case 2 :
        print("Samsung")
 
     case 3 :
        print("Apple")

     case _ :
        print("unknown")


 
