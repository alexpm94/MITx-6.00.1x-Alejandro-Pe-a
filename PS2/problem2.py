balance = 4967
annualInterestRate = 0.04


def lowestPayment(ub,minimumMonthlyPayment):
	for a in range(12):
		mub=ub-minimumMonthlyPayment
		mir=annualInterestRate/12.0
		ub=mub+mir*mub
	print(ub)
	if ub<=0:
		return minimumMonthlyPayment
	else:
		return lowestPayment(balance,minimumMonthlyPayment+10)

print('Lowest Payment:', lowestPayment(3329,10))