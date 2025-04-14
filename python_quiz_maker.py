while True:
    user_question = input("Enter a question: ") #Asks the user for a question

    choices = [] #Initialize list to store choices 

    for i in range(4): #Creates for loop to ask the user 4 times for the choices
        choice = input(f"Enter choice #{i + 1}: ")
        choices.append(choice) #Appends the choice inputs to the CHOICES list

    