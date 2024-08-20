
#Input
user_input = input("Enter a positive integer: ")

while True:
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input = input("The number must be a positive integer. Enter again: ")
    else:
        user_input = input("Invalid input. Please enter a positive integer: ")

print("Collatz Sequence: ")

while number != 1:
    print(number, end=" -> ") #"end" just adds the arrow (->) for appearance purposes. To make the code look nicer.
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
print(1) #so the code stops at 1.

#Basically, if the number is e.g 10, the code would do 10 // 2 == 5. Then (5 x 3) + 1 == 16, then repeat until number == 1.