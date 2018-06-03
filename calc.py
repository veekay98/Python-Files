while True:
    try:
        x = int(input("Please enter first number: "))
        y = int(input("Please enter second number: "))
        break
    except ValueError:
        print("That was no valid number")

print("Input + for add,- for sub,x for mul,/ for div")

op=input("Enter the operator: ")

if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="x":
    print(x*y)
elif op=="/":
    try:
        print(x/y)

    except ZeroDivisionError:
        print("Division by zero not possible")

else:
    print("Invalid Operator")
