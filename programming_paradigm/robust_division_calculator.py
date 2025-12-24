#a function that perfroms division and handles errors
def safe_divide(numerator:float, denominator:float):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        quotient = float(numerator / denominator)
        return f"The result of the division is {quotient}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")