# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6 
# Round the result to 2 decimal places = 33.60 

total_bill = input("Welcome to the tip calculator!\nWhat was the total bill?\n")
percentage = input(f"What percentage tip would you like to give? A percentage tip of {10}, {12} or {15}?\n")
tip_one = 10 
tip_two = 12
tip_three = 15
people = input("How many people will split the bill?\n")
bill_split = total_bill / people * percentage
print("Each person should pay:\n" + format(bill_split))