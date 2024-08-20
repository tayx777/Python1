


#input
hrs = float(input("Enter time duration in hours: "))

#processing
if hrs >= 0:
    min = hrs * 60
    sec = (hrs * 60) * 60
else:
    min = str("Invalid Response")
    sec = str("Invalid Response")
#output
print("The time duration in minutes is: ", min, str("minutes"))
print("The time duration in seconds is: ", sec, str("seconds"))