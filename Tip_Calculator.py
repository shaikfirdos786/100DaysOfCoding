print("Welcome To The Tip Calculator")

total_bill = float(input("What was the total bill? "))
tip = int(
    input("What percentage of tip would you like to give 10 , 12 , or 15 ?"))
split = int(input("How many people to split the bill ? "))
tip_amount = tip / 100
total_tip = total_bill * tip_amount
total_amount = total_bill + total_tip
bill_person = total_amount / split
# each_person = round(bill_person,2)
each_person = "{:.2f}".format(bill_person)
print(f"Each person should pay {each_person}")
