from pyexpat.errors import messages


class NegativeNumberError(Exception):
    def _init_(self, message="Negative number not allowed"):
   self.message = messages
   super(). _init_ (self.message)

def check_position(number):
    if number < 0:
        raise NegativeNumberError(f "received:{number}. Nuber must be positive.")

    else:
        print(f"Number{number} is positive.")

if _name_ == "_main_":
    try:
        check_positive(10)
    except NegativeNumberError as e:
        print(f"Caught an error: {e}")

print("-"*20)

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Caught an error: {e}")

print("_"*20)