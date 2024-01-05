print("Welcom to  the calculator ")
bill = input("What was the total bill? $ ")
percentage = input("What percentage tip  would you like to give? 10, 12, or 15 ? ")
people = input("How many peole to split the bill? ")

tip = float(bill) * (1 + (int(percentage) / 100)) / int(people)

print(f"Each person should pay :${round(tip, 2)}")