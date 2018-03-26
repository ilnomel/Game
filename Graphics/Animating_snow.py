import pygame, random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow Animation")
 
# Loop until the user clicks the close button.
done = False
 
# Initialize empty list
snow_list = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x,y])
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    # Process each snow flake in the list
    for i in range(len(snow_list)):
        # draw the snow flakes
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        
        # move snow flake down one pixel
        snow_list[i][1] += 1
        
        # if the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 400:
            # reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(20)
 
# Close the window and quit.
pygame.quit()