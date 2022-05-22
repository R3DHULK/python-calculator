def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1/num2

print("Select One Operation -\n"

"1. Addition\n"
"2. Subtraction\n"
"3. Multiplication\n"
"4. Division\n")

select = int(input("Select operation form 1,2,3,4 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print (num1, "+",num2, "=", addition(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtraction(num1,num2))
elif select == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif select == 4 :
    print(num1, "/", num2, "=", division(num1,num2))
else:
    print("Invalid Input")