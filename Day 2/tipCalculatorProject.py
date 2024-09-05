print("Welcome to the tip calculator1")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12,or 15? "))
people_to_split = float(input("How any people to split the bill? "))

value_to_pay = round(float((total_bill + (total_bill * ((tip) / 100))) / people_to_split),2)

print(f"Each person should pay: ${value_to_pay}")

