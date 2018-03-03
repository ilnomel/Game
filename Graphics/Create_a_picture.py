import pygame
import math

# Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
BROWN = (135, 30, 30)
    
PI = math.pi

pygame.init()

# Set the width and height of the screen [width, height]
size = (600, 700)
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
    
    # Draw blue sky and green grass
    pygame.draw.rect(screen, BLUE, [0, 0, 600, 500])
    pygame.draw.rect(screen, GREEN, [0, 500, 600, 200])
    
    # Draw clouds
    for x_offset in range(3):
        pygame.draw.circle(screen, WHITE, [70 + x_offset*200, 30], 20)
        pygame.draw.circle(screen, WHITE, [90 + x_offset*200, 30], 20)
        pygame.draw.circle(screen, WHITE, [110 + x_offset*200, 30], 20)
        
    for y_offset in range(1,2):
        for x_offset in range(3):
            pygame.draw.circle(screen, WHITE, [50 + x_offset*200, 30 + y_offset*90], 20)
            pygame.draw.circle(screen, WHITE, [70 + x_offset*200, 30 + y_offset*90], 20)
            pygame.draw.circle(screen, WHITE, [90 + x_offset*200, 30 + y_offset*90], 20)
    
    # Draw trees
    for x_offset in range(4):
        pygame.draw.polygon(screen, GREEN, [[100 + x_offset*150, 350], [75 + x_offset*150, 400], [125 + x_offset*150, 400]])
        pygame.draw.rect(screen, BROWN, [90 + x_offset*150, 461, 20, 39])
        for offset in range(1, 3):
            pygame.draw.polygon(screen, GREEN, [[100 + x_offset*150, 350 +offset*30], [75 + x_offset*150 - offset*15, 400 + offset*30], [125 + x_offset*150 + offset*15, 400 + offset*30]])
            
    # --- Update the screen with what we've drawn --- #
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit
# If this line if forgotten, the program will "hang" on exit if running from IDLE.
pygame.quit()
