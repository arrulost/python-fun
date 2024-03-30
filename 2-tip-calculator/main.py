print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

percentage = input(f"What perchentage tip would you like to give? {10}, {12}, or {15}? ")

people = input("How many people to split the bill? ")

perchentage2 = int(percentage) / 100
tip = float(total_bill) * perchentage2
total_bill2 = float(total_bill) + tip

result = (round(total_bill2 / int(people), 2))
print(f"Each person should pay: ${result}")