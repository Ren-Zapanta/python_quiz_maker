import pygame ##mport the pygame library to create the graphical interface
pygame.init() #Initialize all the Pygame modules

#Sets the window's dimensions
screen_width = 1200
screen_height = 720


screen = pygame.display.set_mode((screen_width, screen_height)) #Creates the window using the initialized dimensions
pygame.display.set_caption("Hacker Terminal") #Name of the window

run = True #control variable that keeps the window running

while run:

    for event in pygame.event.get(): #Check for events like key presses or window closing
        if event.type == pygame.QUIT:  #Verifies if user clicked the close window
            run = False #Closese the window if the user clicks the X button


    pygame.display.update() #Responsible for updating the screen for all changes

pygame.quit() #Close the Pygame window after loop ends