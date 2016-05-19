initBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
initRate = float(raw_input("Enter the annual credit card interest rate as decimal: "))
 
monPay = 0
monRate = initRate / 12
balance = initBalance
 
while balance > 0:
    monPay += 10
    balance = initBalance
    numMonths = 0
    while numMonths < 12 and balance > 0:
        numMonths += 1
        interest = balance * monRate
        balance -= monPay
        balance += interest
 
balance = round(balance, 2)
 
print "RESULT:"
print "Monthly payment to pay off the debt in 1 year: ", monPay
print "Number of months required to pay off the debt: ", numMonths
print "Balance: ", balance
