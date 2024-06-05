#multiplication table
num_multiplier = int(input("Enter number: "))

multiplier = int(input("Ennter the number of times you want to multiply your number: "))

for i in range (1, multiplier + 1):
    result = num_multiplier * i
    print (f"{num_multiplier} x {i} = {result}")