#Tip_Calculator
#Created by Cephas Cardozo
#v1.0

print("Welcome to the Tip Calculator")

total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

tip_calculation = tip / 100 * total + total

split_total = tip_calculation / people

rounded = round(split_total, 2)

message = f"Each person should pay: ${rounded}"

print(message)