principal = float(input("What is the total money borrowed: "))
interestRate = float(input("What is the yearly interest rate, in percent: "))
years = int(input("How many years to repay: "))
monthlyInterest = (interestRate/12)/100
months = years*12
monthlyPayment = principal * ((monthlyInterest * ((monthlyInterest+1)**months))/(((monthlyInterest+1)**months)-1))
print("To pay off a {}$ loan at a yearly interest rate of {}% per year (or {}% per month) in {} years ({} months)\nYou would have to pay {} a month".format(principal, interestRate, monthlyInterest, years, months, monthlyPayment))