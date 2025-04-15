import pygame ##mport the pygame library to create the graphical interface
pygame.init() #Initialize all the Pygame modules

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

while run:

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
            else:
                user_text += event.unicode 
        
           
    screen.fill((0, 0, 0)) #clears the screen with black color

    current_time = pygame.time.get_ticks() #gets the current time since the program was started
    if prompt_index < len(prompt_text) and current_time - last_type_time > typewriter_delay:
        typed_prompt += prompt_text[prompt_index] #This adds the next character to the display
        prompt_index += 1 #After having added the last character, this moves onto the next
        last_type_time = current_time #updates the current_time variable



    typed_surface = base_font.render(typed_prompt, True, ('green')) #this renders the text freen
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