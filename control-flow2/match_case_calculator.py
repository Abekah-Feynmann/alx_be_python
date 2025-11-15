#prompt user for two inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#prompt user for desired operation
operation = input("Choose the operation (+, -, *, /): ")

#perform operation using the match case statements
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        try:
            result = num1 / num2
            print(f"The result is {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
    case _:
        print("Cannot perform operation")