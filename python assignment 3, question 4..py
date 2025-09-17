names = ["Alice","Nancy","Charlie","David","Eve"]
filename = "names.txt"

print(f"writting names to {filename}")
with open(filename,"w") as file:
    for name in names:
        file.write(f"{name}\n")

print(f"/nReading names from{filename}:")
with open(filename,"r") as file:

    for line in file:
        print(line.strip())