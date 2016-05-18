promptBalance = "Enter the outstanding balance on your credit card: "
promptRate = "Enter the annual credit card interest rate as decimal: "

def payOff(balance, annualInterestRate):
	# print "The balance is: " + str(balance) + ", and the interest rate is: " + str(annualInterestRate) + "."
	guess = 10.0
	month = 0
	while balance >= 0:
		month += 1
		balance = balance + (balance * (annualInterestRate / 12))
		balance = balance - guess
		print balance
		
payOff(int(raw_input(promptBalance)), float(raw_input(promptRate)))
