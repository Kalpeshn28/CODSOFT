def add(a,b):
    return a+b
def subs(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Divison by zero is not possible !"
    return a/b


print("Enter task you want to perform :")
print("1.Addition") 
print("2.Substraction") 
print("3.Multiplication") 
print("4.Division") 

choice=int(input("Enter Your choice: "))

if (choice==0 or choice>4):
    print("Invalid Choice!")

else:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    if choice==1:
        print("Result : ",add(num1,num2))
    if choice==2:
        print("Result : ",subs(num1,num2))
    if choice==3:
        print("Result : ",mult(num1,num2))
    if choice==4:
        print("Result : ",div(num1,num2))





