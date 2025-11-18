def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    operations = ['add', 'subtract', 'multiply', 'divide']

    if operation.lower() in operations:       
        if operation.lower() == 'add':
            sum = num1 + num2
            print(sum)
        elif operation.lower() == 'subtract':
            difference = num1 - num2
            print(difference)
        elif operation.lower() == 'multiply':
            product = num1 * num2
            print(product)
        else:
            try:
                quotient = num1 / num2
                print(quotient)
            except ZeroDivisionError:
                print("Divisor for division cannot be zero")

    else:
        raise ValueError("operation parameter must contain only one of the following: add, subtract, multiply, divide")

perform_operation(5, 10, 'divide')
perform_operation(5, 10, 'multiply')
perform_operation(5, 10, 'add')
perform_operation(5, 10, 'subtract')



