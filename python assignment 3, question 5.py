celsius_temps = [0,10,20.5,37,100]

fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

print(f"original celsius temperatures: {celsius_temps}")
print(f"converted fahrenheit temperature: {fahrenheit_temps}")