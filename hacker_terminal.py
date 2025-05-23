import pygame ##mport the pygame library to create the graphical interface
import os
pygame.init() #Initialize all the Pygame modules

intro_stage = "init" #initializes the state of the intro sequence as "init"
intro_texts = { #Dictionary to hold the intro messages for both stages
    "init": "System Initializing...", #The first string to be displayed
    "waiting_key": "Press any key to proceed." #Second message. Displays after three seconds
}

#Handles the typewriter animation
typed_intro_text = ""
intro_index = 0
intro_last_type_time = pygame.time.get_ticks()
intro_typewriter_delay = 45 

intro_start_time = pygame.time.get_ticks() #Records the starting time of the whole intro

pygame.key.set_repeat(400, 30) #Allows keys functionality when held down, instead of pressing it repeatedly

#Sets the window's dimensions
screen_width = 1200
screen_height = 720

base_font = pygame.font.SysFont("consolas", 27) #THe font that the program will be using, along with its size.

user_text = '' #This will contain the user's input

prompt_text = "Please enter a question: " #Prompt that would ask the user to enter a question
typed_prompt = '' #This is where the program will type the prompt, letter by letter.
prompt_index = 0 #This is the index of the next character to type
typewriter_delay = 45 #Delay between each character, set in milliseconds
last_type_time = pygame.time.get_ticks() #The last time that a character was added


screen = pygame.display.set_mode((screen_width, screen_height)) #Creates the window using the initialized dimensions
pygame.display.set_caption("Hacker Terminal") #Name of the window

run = True #control variable that keeps the window running

clock = pygame.time.Clock() #keeps track of time in-between frames

input_stage = "question" #determines what the user is typing for (i.e, question, choices)

#This will hold the inputs (e.g, questions, choices, andthe correct answer)
quiz_data = {
    "question": "",
    "choices": {"A": "", "B": "", "C": "", "D": ""},
    "answer": ""
}

script_dir = os.path.dirname(os.path.abspath(__file__))  #gets the folder at which this file is saved in
file_path = os.path.join(script_dir, "quiz.txt")   #MAkes the full path to the "quiz.txt" file

while run:

#INTRO SEQUENCE

    if intro_stage != "done": #Verifies if the intro-string sequence has not finished yet
        screen.fill((0, 0, 0)) #This fills the screen with the black background

        current_time = pygame.time.get_ticks() #Fetches the time elpased since the program initiates
        elapsed_time = current_time - intro_start_time #Calculates how much time has passed since the intro seqquence started

        current_intro = intro_texts[intro_stage] #gets the current string to be typed on the screen

        if intro_index < len(current_intro) and current_time - intro_last_type_time > intro_typewriter_delay:
            typed_intro_text += current_intro[intro_index] #This adds the next characcter to the text being displayed on the terminal window
            intro_index += 1 #Proceeds to the next character in the string
            intro_last_type_time = current_time #updates the last time that a character was typed

        #Handles the rendering of the text and its color
        intro_surface = base_font.render(typed_intro_text, True, (0, 255, 0))
        screen.blit(intro_surface, (100, 300))

        if intro_stage == "init" and elapsed_time > 3000 and intro_index >= len(current_intro):
            intro_stage = "waiting_key" #updates the stage to wait for any key input
            typed_intro_text = "" #resets the text for the new message
            intro_index = 0 #This resets the character index
            intro_last_type_time = current_time #This is responsible for resetting the time tracker for typing

        pygame.display.update()

        for event in pygame.event.get(): #this loops throuhgh key inputs
            if event.type == pygame.QUIT: #If the user clicks the X button to close the window
                run = False #Terminates the program
            elif event.type == pygame.KEYDOWN and intro_stage == "waiting_key": #Confition when the program reads a key input
                intro_stage = "done" #Moves onto the main interface

        continue
            
#MAIN PROGRAM LOGIC

    for event in pygame.event.get(): #Check for events like key presses or window closing
        if event.type == pygame.QUIT:  #Verifies if user clicked the close window
            run = False #Closese the window if the user clicks the X button

        if event.type == pygame.KEYDOWN: #Lets the user type their own string on the generated terminal itself
            if event.key == pygame.K_BACKSPACE: #Gives function to a specific key
                user_text = user_text[:-1] #Grants the backspace key functionality

            elif event.key == pygame.K_RETURN: #If the user presses enter
                if input_stage == "question":
                    quiz_data["question"] = user_text #This saves the question input
                    user_text = "" #resets the user input
                    prompt_text = "Enter choice A: " #Renders a new prompt; one asking for a choice for the corresponding question
                    typed_prompt = "" #resets the typewriter effect
                    prompt_index = 0 #restarts typing the prompt
                    input_stage = "choice_A" #this updates the current stage of the program

    #CHOICES FOR THE QUESTION INPUT
    #The codes for choices A - D are pretty much just the same, hence the absence of comment lines

                #For choice A
                elif input_stage == "choice_A":
                    quiz_data["choices"]["A"] = user_text  # Save choice A
                    user_text = ""
                    prompt_text = "Enter choice B:"
                    typed_prompt = ""
                    prompt_index = 0
                    input_stage = "choice_B"

                #For choice B
                elif input_stage == "choice_B":
                    quiz_data["choices"]["B"] = user_text  
                    user_text = ""
                    prompt_text = "Enter choice C:"
                    typed_prompt = ""
                    prompt_index = 0
                    input_stage = "choice_C"

                #For choice C
                elif input_stage == "choice_C":
                    quiz_data["choices"]["C"] = user_text  
                    user_text = ""
                    prompt_text = "Enter choice D:"
                    typed_prompt = ""
                    prompt_index = 0
                    input_stage = "choice_D"

                #For choice D
                elif input_stage == "choice_D":
                    quiz_data["choices"]["D"] = user_text  
                    user_text = ""
                    prompt_text = "Enter the correct answer (A, B, C, or D): "
                    typed_prompt = ""
                    prompt_index = 0
                    input_stage = "answer"

                #For correct answer
                elif input_stage == "answer":
                    quiz_data["answer"] = user_text.upper() #sets user_text to uppercase

                    with open(file_path, "a") as file: #opens the file in append mode where the data will be saved at.
                        file.write("Question: " + quiz_data["question"] + "\n") #This will write the question to the file
                        for key in ["A", "B", "C", "D"]: #This will iterate through each of the choices
                            file.write(f"{key}. {quiz_data['choices'][key]}\n") #Formats the choice
                        file.write("Answer: " + quiz_data["answer"] + "\n\n") #Writes the correct answer on the file and adds a spacing for better readability between each question

                    user_text = "" 
                    prompt_text = "Do you want to input another question? (Y/N): " #Asks the user if whether or not they want to input another question
                    typed_prompt = ""
                    prompt_index = 0
                    input_stage = "confirm_continue"
                    quiz_data = {
                        "question": "",
                        "choices": {"A": "", "B": "", "C": "", "D": ""},
                        "answer": ""
                    }

#ASKS IF THE USER WANTS TO INPUT A QUESTION AGAIN

                elif input_stage == "confirm_continue":
                    if user_text.lower() == "y": #If the user says yes
                        user_text = ""  #Clears the input space
                        prompt_text = "Please enter a question: "  #Resets the prompt back to the question input
                        typed_prompt = ""  #Resets the typewriter effect
                        prompt_index = 0  #reset the typewriter index
                        input_stage = "question"  #If the user says yes, it goes baack to entering a question
                        quiz_data = {  #Clears the old data for new input
                            "question": "",
                            "choices": {"A": "", "B": "", "C": "", "D": ""},
                            "answer": ""
                    }
                    elif user_text.lower() == "n":  #if the user says no
                        run = False  #the program will terminate
                    else:
                        # If user input is not valid, prompt again
                        user_text = ""
                        prompt_text = "Invalid input. Please type Y or N:"
                        typed_prompt = ""
                        prompt_index = 0

            else:
                user_text += event.unicode 
        
           
    screen.fill((0, 0, 0)) #clears the screen with black color

    current_time = pygame.time.get_ticks() #gets the current time since the program was started
    if prompt_index < len(prompt_text) and current_time - last_type_time > typewriter_delay:
        typed_prompt += prompt_text[prompt_index] #This adds the next character to the display
        prompt_index += 1 #After having added the last character, this moves onto the next
        last_type_time = current_time #updates the current_time variable

    typed_surface = base_font.render(typed_prompt, True, ('green')) #this renders the text Green
    screen.blit(typed_surface, (100, 250)) #This assigns x and y coordinates to the prompt; placing it right above the input line



    #These are responsible for rendering what the user has typed on the screen
    text_surface = base_font.render(user_text, True, (0, 255, 0))
    screen.blit(text_surface, (100, 300))

    time_now = pygame.time.get_ticks() #Fetches the current time since the program was started (in milliseconds)

    if (time_now // 500) % 2 == 0:
        text_width = text_surface.get_width() #Determines the width of the text
        cursor_x = 100 + text_width #Places the blinking cursor right after the last character
        cursor_y = 300 #Places the blinking cursor in the same y axis coordinate as the text
        pygame.draw.rect(screen, (0, 255, 0), (cursor_x, cursor_y, 3.5, base_font.get_height())) #Draws the blinking object; contains the necessary dimensions and coordinates

    pygame.display.update() #Responsible for updating the screen for all changes
    clock.tick(60) #Caps the program's framerate to 60 fps

pygame.quit() #Close the Pygame window after loop ends