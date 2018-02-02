updBalance=balance
l=balance/12
h=balance*(annualInterestRate+1)/12
a=0
mf=(h+l)/2.0
guess=False
epsilon=0.01

while guess==False:

     for month in range(12):
        Mir=annualInterestRate/ 12.0
        uBalance=updBalance-mf
        updBalance=round(uBalance+Mir*uBalance,2)

     if updBalance<0:
         h=mf
         updBalance=balance
    
     elif updBalance>epsilon:
         l=mf
         updBalance=balance
     else:
        guess=True
    
     mf=(h+l)/2.0
        
print('Lowest Payment: ',round(mf,2))