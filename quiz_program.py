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
