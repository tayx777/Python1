

#input
Subject1_input = input("Enter your grade for Subject 1: ")
Subject2_input = input("Enter your grade for Subject 2: ")
Subject3_input = input("Enter your grade for Subject 3: ")

#processing
if Subject1_input.isdigit() and Subject2_input.isdigit() and Subject3_input.isdigit():
    subject1 = int(Subject1_input)
    subject2 = int(Subject2_input)
    subject3 = int(Subject3_input)

    if 0 <= subject1 <= 100 and 0 <= subject2 <= 100 and 0 <= subject3 <= 100:

        grade = (subject1 + subject2 + subject3) / 3

        if 90 <= grade <= 100:
            #output
            print("Your grade is an A.")
        elif 80 <= grade <= 89:
            #output
            print("Your grade is a B.")
        elif 70 <= grade <= 79:
            #output
            print("Your grade is a C.")
        elif 60 <= grade <= 69:
            #output
            print("Your grade is a D.")
        elif 0 <= grade < 60:
            #output
            print("Your grade is an F.")
        else:
            #output
            print ("Error. Please enter the correct grade for each subject.")
    else:
        #output
        print("Error: Please enter a correct grade for each subject.")
else:
    #output
    print("Error: Please enter a number for your grade.")