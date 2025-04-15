import pygame ##mport the pygame library to create the graphical interface
pygame.init() #Initialize all the Pygame modules

pygame.key.set_repeat(400, 30) #Allows keys functionality when held down, instead of pressing it repeatedly

#Sets the window's dimensions
screen_width = 1200
screen_height = 720

base_font = pygame.font.SysFont("consolas", 27) #THe font that the program will be using, along with its size.

user_text = '' #This will contain the user's input


screen = pygame.display.set_mode((screen_width, screen_height)) #Creates the window using the initialized dimensions
pygame.display.set_caption("Hacker Terminal") #Name of the window

run = True #control variable that keeps the window running

clock = pygame.time.Clock() #keeps track of time in-between frames

while run:

    for event in pygame.event.get(): #Check for events like key presses or window closing
        if event.type == pygame.QUIT:  #Verifies if user clicked the close window
            run = False #Closese the window if the user clicks the X button
        if event.type == pygame.KEYDOWN: #Lets the user type their own string on the generated terminal itself
            if event.key == pygame.K_BACKSPACE: #Gives function to a specific key
                user_text = user_text[:-1] #Grants the backspace key functionality
            else:
                user_text += event.unicode 
        

       
    screen.fill((0, 0, 0)) #clears the screen with black color

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