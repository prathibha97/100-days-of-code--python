print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
bill_after_tip = total_bill + total_bill * tip
split = float(input("How many people to split the bill? "))
pay = bill_after_tip / split
final_amount="{:.2f}".format(pay)
print(f"Each person should pay ${final_amount}") 
