# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
input_bill = float(input("What was the total bill? "))
input_tip = int(input("What percentage tip would you like to give ? 10, 12 or 15? "))
input_persons= int(input("How many people to split the bill? "))

tip = input_tip / 100 * input_bill
result = (input_bill + tip) / input_persons
print(f"Each person should pay: ${round(result, 2)}")
# rounded_result = "{:.2f}".format(result)
# print(f"Each person should pay: ${rounded_result}")
