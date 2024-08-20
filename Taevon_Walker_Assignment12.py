

pattern_input = input("Enter a number of rows: ")

while True:
    if pattern_input.isdigit():
        pattern = int(pattern_input)
        if pattern > 1:
            break
        else:
            pattern_input = input("The number of rows must be a positive integer greater than 1 to create a right triangle. Enter again: ")
    else:
        pattern_input = input("Invalid input. Please enter a positive integer: ")

for p in range(1, pattern + 1):
    print("*" * p)

