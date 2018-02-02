'''
	This program returns de remaining balance
	at the end of the year of a credit card
	payment, it needs the pirncipal balance,
	annual interest rate an the montlhly payment
	rate.
'''


ub = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for a in range(12):
    monthlyInterestRate=annualInterestRate/12.0
    minimumMonthlyPayment=monthlyPaymentRate*ub
    mub=ub-minimumMonthlyPayment
    ub=mub+monthlyInterestRate*mub

print('Remaining balance:',round(ub,2))
    