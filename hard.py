loan= eval(input("Enter loan amount: "))
loan_period= eval(input("Enter loan period for years: "))
loan_period *= 12
balance = loan
principal = loan/ loan_period
print("Payment Schedule")
print("Month\t|\tMonthly Payment\t|\tInterest\t|\tPrincipal\t|\tRemaining Balance\t|")

for i in range(1, loan_period+1, 1):
    balance-= principal
    interest = balance * 0.03
    monthly= principal + interest
    print(f"{i}\t|\t{round(principal, 2)}\t\t|\t{round(balance, 2)}\t\t|\t{round(interest, 2)}\t\t|\t{round(monthly, 2)}")