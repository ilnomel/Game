import pygame

#initialize the game engine
pygame.init()

# Define some colors
# these are constance, therefore they are capitalized
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello!")

#loop until the user clicks the close button
done = False

#used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ---------------
while not done:
    # ---- Main Event Loop
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if user clicked close
            done = True #flag used to indicate we exit the loop
    
    # ---- Game logic should go here
    
    # ---- Drawing code should go here
    #First, clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    # ---- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # ---- Limit to 60 frames per second
    clock.tick(60)
    
    #close the window and quit
    pygame.quit()