#Asks the users to enter a question and four corresponding choices for it

while True:
    user_question = input("Enter a question: ") #Asks the user for a question

    choices = [] #Initialize list to store choices 

    for i in range(4): #Creates for loop to ask the user 4 times for the choices
        choice = input(f"Enter choice #{i + 1}: ")
        choices.append(choice) #Appends the choice inputs to the CHOICES list

#A loop for determining the correct answer for the question input

    while True: 
        try: 
            correct_choice = int(input(f"Which one is the correct answer? (1-4): ")) #Asks the user which of the choice input is the correct answer for the corresponding question
            if 1 <= correct_choice <= 4: #Verifies if the correct_choice input is within the numerical range of 1 and 4
                break #breaks loop if the input is valid 
            else:
                print("Please enter a number between 1 to 4") #Prints if the input is not within range

        except ValueError:
            print("Please enter a valid input") #Prints if the input is non-numeric; invalid

#This part is responsible for writing data onto the text file

    with open(r"C:\Users\renza\OneDrive\Documents\School\College\2nd Semester\Object Oriented Programming\Programs\python_quiz_maker\quiz.txt", "a") as file: #This opens the file wherein the data 
        file.write(f"Question: {user_question} \n") #This writes the actual question onto the text file
        for i, choice in enumerate(choices, start=1): #Loops over each of the 4 choice inputs of the user
            file.write(f"{i}. {choice}\n") #This writes the choices of a given question on the text file with the assigned number up front
        file.write(f"Correct answer: {correct_choice} \n") #This writes the correct answer for the given question

#This parts is responsible for looping back to the original prompt for if the user would like to input another question and a set of answers

    another_question = input("Would you like to add another question? (Y/N): ") #Asks if the user would like to add another question
    if another_question.lower() not in ['yes', 'y']: #Verifies for input validity
        #Prints if user decides to exit
        print("Saving to 'quiz.txt!")
        print("Exiting")
        break
        

    
            




    