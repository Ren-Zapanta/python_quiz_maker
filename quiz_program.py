
import pygame
import sys
import os
import time
import random

def typewriter(text, current, index, last_time, delay):
    now = pygame.time.get_ticks()  # Get current time
    if index < len(text) and now - last_time > delay:
        current += text[index]  # Add next character
        index += 1
        last_time = now
    return current, index, last_time

pygame.init() #Initializes Pygame modules

script_dir = os.path.dirname(os.path.abspath(__file__))  #gets the folder at which this file is saved in
file_path = os.path.join(script_dir, "quiz.txt")   #MAkes the full path to the "quiz.txt" file

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
    "quiz_init": "This quiz will determine if you get to live or not.",#Second intro stage
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
            answer_line = lines[5].strip().upper() #the last line is the correct answer
            answer = answer_line[-1]
            questions.append({"question": question, "choices": choices, "answer": answer})
        
    return questions

questions = load_questions(file_path) #Loads the question from the text file
random.shuffle(questions) #Randomizes the questions 

current_question_index = 0 #Keeps track of which questions the user is answering
user_answer = "" #keeps the user's input
feedback = ""  #stores whether the answer inputed is correct or not
feedback_timer = 0 #records when th feedback was shown


#animation trackers for the texts to be displayed on the terminal
typed_q = ""
typed_q_index = 0
typed_q_time = pygame.time.get_ticks()
typed_choices = ["", "", "", ""]
typed_choice_index = [0, 0, 0, 0]
typed_choice_time = [pygame.time.get_ticks()] * 4
typed_feedback = ""  # stores animated feedback text
typed_feedback_index = 0
typed_feedback_time = pygame.time.get_ticks()

q_typing_delay = 30  #interval between letters


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

        elif intro_stage == "quiz" and event.type == pygame.KEYDOWN:
            key = event.unicode.upper() #Converts the pressed key into upper case
            if key in ["A", "B", "C", "D"]: #only accepts thses characters
                user_answer = key #saves the user's input
                correct_answer = questions[current_question_index]["answer"] #gets the correct answer
                if user_answer == correct_answer: #prints corresponding statement if the user is either correct or not
                    feedback = "You're correct."
                else:
                    feedback = "You are wrong."
                feedback_timer = pygame.time.get_ticks()


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
                if now - intro_start_time > 4500:
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
        typed_q, typed_q_index, typed_q_time = typewriter( question_data["question"], typed_q, typed_q_index, typed_q_time, q_typing_delay)
        screen.blit(base_font.render(typed_q, True, green), (100, 260))

        for i, choice in enumerate(question_data["choices"]):
            typed_choices[i], typed_choice_index[i], typed_choice_time[i] = typewriter(
                choice, typed_choices[i], typed_choice_index[i], typed_choice_time[i], q_typing_delay
            )
            screen.blit(base_font.render(typed_choices[i], True, green), (120, 300 + i * 40))
                

        if feedback: #tells the user if they are either correct or incorrect
            typed_feedback, typed_feedback_index, typed_feedback_time = typewriter(
                feedback, typed_feedback, typed_feedback_index, typed_feedback_time, q_typing_delay
            )

            screen.blit(base_font.render(typed_feedback, True, green), (100, 500))

            if pygame.time.get_ticks() - feedback_timer > 2000:
                feedback = "" #resets the feedback variable
                typed_feedback = ""
                typed_feedback_index = 0 
                typed_feedback_time = pygame.time.get_ticks()

                current_question_index += 1 #proceeds with the next question
                user_answer = "" #resets the user answer
                typed_q = ""  # clear previous typed question
                typed_q_index = 0  # reset character index for typing
                typed_choices = ["", "", "", ""]
                typed_choice_index = [0, 0, 0, 0]
                typed_choice_time = [pygame.time.get_ticks()] * 4

                if current_question_index >= len(questions):
                    intro_stage = "end"



    if intro_stage != "quiz":
        screen.blit(base_font.render(typed_intro_text, True, green), (125, screen_height // 2)) #renders the text on the terminal
    

    pygame.display.flip() #updates the display for the latest changes
            


pygame.quit()
sys.exit()
