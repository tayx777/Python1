

#input
user_input = input("Enter a string: ")

string = user_input.replace(" ","").lower()  #The .replace() allows me to remove any spaces that might interfere with the output
                                                         #And the .lower() just allows the code to bypass any inconsistency in the capitalization of letters
                                                         #For example, "Madam" doesn't have to be typed out as "MadaM" to be True. The code will accept it.

left = 0                #Starting point/first index
right = len(string) - 1 #If we didn't subtract 1 from the length, the right pointer would be set to an index that doesn't exist in the string since Python indexes start from 0, not 1.
                        #Subtracting 1 gives us the last index in our string. For ex, "hello" has 5 characters, so the total length is 5.
                        #But the last character "o" is INDEX 4 (h e l l o), so INDEX 5 doesn't exist.
                        #                                       0 1 2 3 4
                        #We would have gotten an error code had we not subtracted 1 from our length

palindrome = True
while left < right:     # the right index has to be greater than the left index in order for the code to work
    if string[left] != string[right]:
        palindrome = False
        break
    left += 1           #This will make the first character move to the right by 1
    right -= 1          #This will make the last character move to the left by 1
if palindrome:
    print(f"{user_input} is a palindrome.")         #The "f'{}'" allows you to place the user's input value into the string for a cleaner output response.
else:
    print(f"{user_input} is not a palindrome.")