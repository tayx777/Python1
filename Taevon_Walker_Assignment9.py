

#input
char_input = input("Enter a single character: ")

#processing ... .isalpha() is a module in python to signify a letter
if len(char_input) == 1 and char_input.isalpha():
    char = char_input.lower()
    if char in "aeiou":
        #output
        print("The character is a vowel.")
    else:
        #output
        print("The character is a consonant.")
else:
    if len(char_input) != 1:
        #output
        print("Error: Please enter only one character.")
    else:
        #output
        print("Error: The input is not a letter")