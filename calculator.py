print("===== SIMPLE CALCULATOR =====")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operation = input("choose an poeration(+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operation!")
    
