import pygame
import math

# Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

PI = math.pi

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My picture")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ----------#
while not done:
    # --- Main event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # --- Drawing code should go here
    # First, clear the screen to white. 
    # Don't put other drawing commands above this
    screen.fill(WHITE)
    
    # --- Update the screen with what we've drawn --- #
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit
# If this line if forgotten, the program will "hang" on exit if running from IDLE.
pygame.quit()
