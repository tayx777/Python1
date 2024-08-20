

#input ... could also diplay int(input("...: ") See Line 8
age_input = input("Enter your age: ")

#processing ... .isdigit checks if entered character is a number
if age_input.isdigit():
    age = int(age_input)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior citizen")
    else:
        print("Error: Age must be a positive number.")

else:
    print("Error: Invalid input. Please enter a positive number.")