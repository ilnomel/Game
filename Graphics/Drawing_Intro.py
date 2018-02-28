import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    # draw a rectangle
    pygame.draw.rect(screen, RED, [55, 50, 20, 25])
    
    # draw a line from (0,0) to (100,100)
    # that is 5 pixels wide                    
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    
    # draw several lines from (0,10) to (100, 100) 
    # 5 pixels wide using for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10+y_offset], [100, 110+y_offset], 5)
    
    # use cosine and sine to draw
    for i in range(200):
        radians_x = i/20
        radians_y = i/6
        
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200
        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)
        
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
pygame.quit()