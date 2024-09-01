
#Challenge: Write the function using recursion.

# Create a function named is_palindrome that takes a string as input
# and returns True if it is a palindrome, and False otherwise.

def is_palindrome(string):

    string = string.replace(" ", "").lower()

    if len(string) <= 1:
        return "Is a palindrome"

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return ("Is not a palindrome")

print(is_palindrome(input("Enter a string: ")))