

#input
year_input = (input("Enter a year: "))

#processing
if year_input.isdigit():
    year = int(year_input)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        #output
        print("This is a leap year.")
    else:
        #output
        print("This is not a leap year.")
else:
    #output
    print("Error: Please type in a positive numerical value.")