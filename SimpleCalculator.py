
def add(num1,num2):
     return num1 + num2

def sub(num1,num2):
     return num1 - num2 

def multiply(num1,num2):
     return num1 * num2  

def divide(num1,num2):
     if num2!=0:
       return num1 / num2 
     else:
          print("Second number is 0.\nPlease select other numbers.")  

print("Welcome to the Calculator\n"
      "Please select a operation:\n"
      "1. Addition\n" 
      "2. Substraction\n" 
      "3. Multiplication\n" 
      "4. Division\n") 

select = int(input("Select a operation from 1,2,3,4:")) 

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if select == 1:
     print(number1, "+", number2, "= ", 
           add(number1, number2))

elif select == 2:
     print(number1, "-", number2, "= ", 
           sub(number1, number2)) 
     
elif select == 3:
     print(number1, "*", number2, "= ", 
           multiply(number1, number2))
     
elif select == 4:
     print(number1, "/", number2, "= ", 
           divide(number1, number2))

else:
     print("Invalid operation! Please select again!")
     
