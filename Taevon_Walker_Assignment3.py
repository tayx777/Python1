

#input for BMI (Body Mass Index)
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))

#processing
bmi = weight / (height ** 2)

print("Your body mass index (bmi) is: " + str(bmi))