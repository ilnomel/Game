import pygame
 
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

# Starting position of white square
x_pos_w = 50
y_pos_w = 50

# Speed and direction of white square
x_change_w = 5
y_change_w = 5

# Starting position of red square
x_pos_r = 500
y_pos_r = 50

# Speed and direction of red square
x_change_r = 6
y_change_r = 6
 
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
    
    # Draw the rectangles
    pygame.draw.rect(screen, WHITE, [x_pos_w, y_pos_w, 50, 50])
    pygame.draw.rect(screen, RED, [x_pos_r, y_pos_r, 50, 50])
    
    # Move the rectangles 
    x_pos_w += x_change_w
    y_pos_w += y_change_w
    
    x_pos_r += x_change_r
    y_pos_r += y_change_r
    
    # Bounce the rectangles if needed
    if x_pos_w > 650 or x_pos_w < 0:
        x_change_w = x_change_w * -1
    if y_pos_w > 450 or y_pos_w < 0:
        y_change_w = y_change_w * -1
        
    if x_pos_r > 650 or x_pos_r < 0:
        x_change_r = x_change_r * -1
    if y_pos_r > 450 or y_pos_r < 0:
        y_change_r = y_change_r * -1 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()