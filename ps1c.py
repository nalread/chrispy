initBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
initRate = float(raw_input("Enter the annual credit card interest rate as decimal: "))

balance = initBalance
low = initBalance / 12
high = balance * (1 + (initRate /12)) ** 12.0 / 12.0
monPay = round((low + high) / 2, 2)
monRate = initRate / 12
 
while balance > 0:
    monPay += 0.01
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
