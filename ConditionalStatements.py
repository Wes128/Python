# if....else... statement

votes = 0
if votes >50000:
    print("You are elected as President")
    print("Starting 2024 upto 2028")
else:
    print("You are not elected as President")

marks = 101
if marks > 80 and marks <=100:
    print("You have a grade A")
elif marks >70 and marks <=80:
    print("You have a grade B")
elif marks > 60 and marks <=70:
    print("You have a grade C")
elif marks > 50 and marks <=60:
    print("You have a grade D")
elif marks > 40 and marks <=50:
    print("You have a grade E")
elif marks > 20 and marks <=40:
    print("You have a grade F")
elif marks > 0 and marks <=20:
    print("You have a failed")
else:
    print("Enter a value between 0 and 100")


# create an atm machine that awards discount to users depending on their
# withdrawal amount and display the total amount inclusive of the discounts.
# Withdrawal above 10,000 award a discount of 15%,
# withdrawal above 5000 give a discount of 10%
# and lastly a withdrawal of above 2000 give a discount of 5%

amount= int(input("Enter withdrawal amount: "))
if amount > 10000:
    discount = (15/100 * amount)
    print(discount)
elif    amount > 5000:
    discount = (10/100 * amount)
    print(discount)
elif amount > 2000:
    discount = (5/100 *amount)
    print(discount)
else:
    print("no discount")


