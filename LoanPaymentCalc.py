# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("How will your monthly payment be, in dollars?\n"))
months = int(input("How many months do yo want to see results for?\n"))

monthy_rate = apr/100/12
for i in range(months):
    interest_paid = money_owed * monthy_rate
    money_owed += interest_paid
    if (money_owed - payment) <= 0:
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
    money_owed -= payment
    print("Paid", payment, "of which", interest_paid, "was interest.", end=" ")
    # end so both print statements are on the same line
    print("Now I owe", money_owed)