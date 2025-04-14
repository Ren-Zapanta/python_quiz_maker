while True:
    user_question = input("Enter a question: ") #Asks the user for a question

    choices = [] #Initialize list to store choices 

    for i in range(4): #Creates for loop to ask the user 4 times for the choices
        choice = input(f"Enter choice #{i + 1}: ")
        choices.append(choice) #Appends the choice inputs to the CHOICES list

    while True: #A loop for determining the correct answer for the question input
        try: 
            correct_choice = int(input(f"Which one is the correct answer? (1-4): ")) #Asks the user which of the choice input is the correct answer for the corresponding question
            if 1 <= correct_choice <= 4: #Verifies if the correct_choice input is within the numerical range of 1 and 4
                break #breaks loop if the input is valid 
            else:
                print("Please enter a number between 1 to 4") #Prints if the input is not within range

        except ValueError:
            print("Please enter a valid input") #Prints if the input is non-numeric; invalid

    