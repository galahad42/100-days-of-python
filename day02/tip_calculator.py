print("Welcome to the tip calculator.")

t_bill = float(input("What was the total bill? $"))
tip    = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split  = int(input("How many people to split the bill? "))
per_person = (t_bill + (tip/100)*t_bill)/split

print(f"Each person should pay: ${round(per_person, 2)}")