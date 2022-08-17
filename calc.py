#Simple Python Calulator
try:
    num1 = int(input("First Number?:"))
    num2 = int(input("Second Number?:"))
    op = str(input("Division=/ Multiplication=* Subtraction=- Addition=+:"))
except:
    num1=1
    num2=2
    op="+"
output = "error"
if op == "+":
    output= (num1 + num2)
if op == "/":
    output= (num1 // num2)
if op == "-":
    output= (num1 - num2)
if op == "*":
    output= (num1 * num2)
print(str(output))
