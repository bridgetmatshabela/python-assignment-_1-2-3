def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error : Cannot divide by zero.")
        return None
    except TypeError:
        print("Error : Invalid input types. Both numerator and denominator must be numbers.")
        return None