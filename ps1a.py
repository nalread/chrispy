balance = float(raw_input("Enter the outstanding balance on your credit card: "))
ann_int_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
min_mon_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
 
# print balance, ann_int_rate, min_mon_rate
 
# print min_mon_pay, interest_paid, principle_paid
 
for i in range(1, 13):
    print "Month " + str(i)
    min_mon_pay = round(min_mon_rate * balance, 2)
    interest_paid = round(ann_int_rate / 12 * balance, 2)
    principle_paid = round(min_mon_pay - interest_paid, 2)
    balance = round(balance - principle_paid, 2)
    print "Minimal monthly payment: " + str(min_mon_pay)
    print "Principle paid: " + str(principle_paid)
    print "Remaining balance: " + str(balance)
