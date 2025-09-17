import random

def generate_random_numbers(count,min_val,max_val):

numbers = [random.randint(min_val,max_val) for _ in rang(count)]
   return numbers

   def calculate _average(numbers):

   if not numbers:
       return 0.0
   return sum(numbers) / len(numbers)

def main():
    num_count = 10
    min_value = 1
    max_value = 100

    random_integers = generate_random_numbers(num_count,min_value,max_value)
    print(f"generated random integers:{random_integers}")

    average_value = calculate_average(random_integers)
    print(f"The average of the generated numbers is:{average_value:.2f}")

    if _name_=="_main_":
        main()
