import pygame
import sys
import time
import random

pygame.init() #Initializes Pygame modules

base_font = pygame.font.SysFont("consolas", 27) #THe font that the program will be using, along with its size.

#Sets the window's dimensions
screen_width = 1200
screen_height = 720
pygame.display.set_caption("Hacker Terminal") #name of the window

screen = pygame.display.set_mode((screen_width, screen_height))

green = (0, 255, 0)  #color for the green text
black = (0, 0, 0) #terminal's background color

intro_stage = "init" #keeps track of which phase in the intro sequence is in

intro_text = {
    "init": "System starting, please wait...", #First intro stage 
    "quiz_init": "Quiz initialized.",#Second intro stage
    "waiting_key": "Press any key to continue." #Third intro stage

}
#Handles the intro text animation
typed_intro_text = "" #stores typed characters
intro_index = 0 #keeps track of what character to type next
intro_last_type_time = pygame.time.get_ticks() #records when the last character was typed
intro_typewriter_delay = 45 #interval between each letter (in milliseconds)

intro_start_time = pygame.time.get_ticks()  #records when the intro started

def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip() #Reads all texts in the given thext file
    
    blocks = content.split("\n\n") #splits questions
    questions = [] #list to store eqach question block

    for block in blocks:
        lines = block.strip().split("\n") #this splits each question block into individual lines
        if len(lines) >= 6: #ensures black has the complete question, its choices, and the correct answer
            question = lines[0] #questions are the first line
            choices = lines[1:5] #Next 4 lines are the choices
            answer = lines[5].strip().upper() #the last line is the correct answer
            questions.append({"question": question, "choices": choices, "answer": answer})
        
    return questions

questions = load_questions("quiz.txt") #Loads the question from the text file
random.shuffle(questions) #Randomizes the questions 

current_question_index = 0 #Keeps track of which questions the user is answering
user_answer = "" #keeps the user's input
feedback = ""  #stores whether the answer inputed is correct or not
feedback_timer = 0 #records when th feedback was shown





#The loop below will keep the program running unless the user decides to close
run = True

while run:
    screen.fill(black)
    now = pygame.time.get_ticks()

    for event in pygame.event.get(): #checks for key presses as 'events'
        if event.type == pygame.QUIT: #checks if the 'event' is for closing the window

            run = False #stops the loop
            screen.fill(black)
            pygame.display.flip()

        elif intro_stage == "waiting_key" and event.type == pygame.KEYDOWN:
            intro_stage = "quiz"
            typed_intro_text = ""
            intro_index = 0
            intro_start_time = pygame.time.get_ticks()

    if intro_stage == "init": #Handles the intro anmiation
        if now - intro_last_type_time > intro_typewriter_delay: #Checks if enough time has passed to show the next letter
            if intro_index < len(intro_text["init"]):
                typed_intro_text += intro_text["init"][intro_index] #this adds the next character from the intro message
                intro_index += 1
                intro_last_type_time = now
            else:
                #if the full intro has been displayed, wait for three seconds before proceeding
                if now - intro_start_time > 3000:
                    intro_stage = "quiz_init" #proceeds to the next phase
                    typed_intro_text = "" #resets the displayed text 
                    intro_index = 0 #resets the index
                    intro_start_time = now #resets the ti mer

    elif intro_stage == "quiz_init": #second stage of the intro
        if now - intro_last_type_time > intro_typewriter_delay:
            if intro_index < len(intro_text["quiz_init"]):
                typed_intro_text += intro_text["quiz_init"][intro_index]
                intro_index += 1
                intro_last_type_time = now
            else:
                if now - intro_start_time > 2000:
                    intro_stage = "waiting_key" 
                    typed_intro_text = "" 
                    intro_index = 0 
                    intro_start_time = now 

    elif intro_stage == "waiting_key": #third stage of the intro
        if now - intro_last_type_time > intro_typewriter_delay:
            if intro_index < len(intro_text["waiting_key"]):
                typed_intro_text += intro_text["waiting_key"][intro_index]
                intro_index += 1
                intro_last_type_time = now
        
    elif intro_stage == "quiz":
        question_data = questions[current_question_index] #fetches the current questions data
        screen.blit(base_font.render(question_data["question"], True, green), (100, 100)) #displays thequestion


        for i, choice in enumerate(question_data["choices"]): #displays the 4 choices
            screen.blit(base_font.render(choice, True, green), (120, 160 + i * 40))

        if feedback: #tells the user if they are either correct or incorrect
            screen.blit(base_font.render(feedback, True, green), (100, 350))

            if pygame.time.get_ticks() - feedback_timer > 2000:
                feedback = "" #resets the feedback variable
                current_question_index += 1 #proceeds with the next question
                user_answer = "" #resets the user answer

                if current_question_index >= len(questions):
                    intro_stage = "end"



    if intro_stage != "quiz":
        screen.blit(base_font.render(typed_intro_text, True, green), (125, screen_height // 2)) #renders the text on the terminal
    else:
        #displays the question
        question_data = questions[current_question_index] #retrieves the question's data from the questions list above
        screen.blit(base_font.render(question_data["question"], True, green), (100, 100))

        #displays the choices on the terminal
        for i, choice in enumerate(question_data["choices"]):
            screen.blit(base_font.render(choice, True, green), (120, 160 + i * 40))

        #lets the user know if they are correct or not
        if feedback:
            screen.blit(base_font.render(feedback, True, green), (100, 350))

    pygame.display.flip() #updates the display for the latest changes
            


pygame.quit()
sys.exit()