

#input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate(%): "))
time = float(input("Enter time period (in years): "))

#processing
interest = (principal * rate * time) / 100

#output
print("The simple interest is: ", interest, str("%"))