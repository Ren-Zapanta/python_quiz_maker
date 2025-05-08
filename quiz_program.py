import pygame
import sys
import time

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
    "waiting_key": "Press any key to continue." #Second intro stage

}
#Handles the intro text animation
typed_intro_text = "" #stores typed characters
intro_index = 0 #keeps track of what character to type next
intro_last_type_time = pygame.time.get_ticks() #records when the last character was typed
intro_typewriter_delay = 45 #interval between each letter (in milliseconds)

intro_start_time = pygame.time.get_ticks()  #records when the intro started

#The loop below will keep the program running unless the user decides to close

run = True

while run:

    now = pygame.time.get_ticks()

    for event in pygame.event.get(): #checks for key presses as 'events'
        if event.type == pygame.QUIT: #checks if the 'event' is for closing the window

            run = False #stops the loop
            screen.fill(black)
            pygame.display.update()

    if intro_stage == "init": #Handles the intro anmiation
        if now - intro_last_type_time > intro_typewriter_delay: #Checks if enough time has passed to show the next letter
            if intro_index < len(intro_text["init"]):
                typed_intro_text += intro_text["init"][intro_index] #this adds the next character from the intro message
                intro_index += 1
                intro_last_type_time = now
            else:
                #if the full intro has been displayed, wait for three seconds before proceeding
                if now - intro_start_time > 3000:
                    intro_stage = "waiting_key" #proceeds to the next phase
                    typed_intro_text = "" #resets the displayed text 
                    intro_index = 0 #resets the index
                    intro_start_time = now #resets the ti mer

    elif intro_stage == "waiting_key":
        if now - intro_last_type_time > intro_typewriter_delay:
            if intro_index < len(intro_text["waiting_key"]):
                typed_intro_text += intro_text["waiting_key"][intro_index]
                intro_index += 1
                intro_last_type_time = now

        for event in pygame.event.get(): #checks for any key presses
            if event.type == pygame.QUIT:
                run = False #terminates the program if the window is closed

    screen.fill(black)
    screen.blit(base_font.render(typed_intro_text, True, green), (40, screen_height // 2)) #renders the text on the screen
    pygame.display.update()
            


pygame.quit()
sys.exit()