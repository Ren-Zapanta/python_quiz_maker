import pygame
import sys
import time

pygame.init() #Initializes Pygame modules

base_font = pygame.font.SysFont("consolas", 27) #THe font that the program will be using, along with its size.

#Sets the window's dimensions
screen_width = 1200
screen_height = 720
pygame.display.set_caption("Hacker Terminal") #name of the window

green = (0, 255, 0)  #color for the green text
black = (0, 0, 0) #terminal's background color

intro_stage = "init" #keeps track of which phase in the intro sequence is in

intro_text = {
    "init": "System starting, please wait.", #First intro stage 
    "waiting_key": "Press any key to continue." #Second intro stage

}
#Handles the intro text animation
typed_intro_text = "" #stores typed characters
intro_index = 0 #keeps track of what character to type next
intro_last_type_time = pygame.time.get_ticks() #records when the last character was typed
intro_typewriter_delay = 45 #interval between each letter (in milliseconds)

intro_start_time = pygame.time.get_tiks()  #records when the intro started




