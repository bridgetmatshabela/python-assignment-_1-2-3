def classify_number():
    while True:
        try:
            num_str = input("Enter an integer: ")
            number = int(num_str)
            break # Exit the loopif a valid integer is entered
        except ValueError:
            print("Invalid input.Please enter a valid integer.")

    if number > 0 :
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return"Zero"