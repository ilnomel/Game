import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = math.pi
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
    pygame.draw.rect(screen, RED, [300, 300, 250, 100],2)
    
    # draw an ellipse, using a rectangle as the outside boundary
    pygame.draw.ellipse(screen, BLACK, [300, 300, 250, 100],2)
    
    # draw an arc as part of an ellipse. use radians to determine what angle to draw
    pygame.draw.arc(screen, GREEN, [300, 300, 250, 100], PI/2, PI, 2)
    pygame.draw.arc(screen, BLACK, [300, 300, 250, 100], 0, PI/2, 2)
    pygame.draw.arc(screen, RED, [300, 300, 250, 100], 3*PI/2, 2*PI, 2)
    pygame.draw.arc(screen, BLUE, [300, 300, 250, 100], PI, 3*PI/2,2)
    
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
        
    #drawing multiple x
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset-10, 90],2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset-10, 100],2)
        
    #draw triangle using polygon command
    pygame.draw.polygon(screen, BLACK, [[500, 100], [400, 200], [500, 200]], 5)  
    
    #drawing text
    
    # select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    # render the text. "True" means anti-aliased text
    #creates an image of the letters, but does not put it on screen yet
    text = font.render("My text", True, BLACK)
    
    #put the image of text on the screen at 300, 250
    screen.blit(text, [300, 250])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
pygame.quit()