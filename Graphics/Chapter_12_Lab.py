"""
Pygame base template for opening a window, done with functions
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import random 
 
# The use of the main function is described in Chapter 9.
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Rectangle():
    def __init__(self):
        self.x = 0 #x position
        self.y = 0 #y position
        self.height = 0
        self.width = 0
        self.change_x = 0
        self.change_y = 0
        self.colour_1 = 0
        self.colour_2 = 0
        self.colour_3 = 0
        
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
 
    def draw(self, screen):
        pygame.draw.rect(screen, [self.colour_1, self.colour_2, self.colour_3], [self.x, self.y, self.width, self.height])
    
class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, [self.colour_1, self.colour_2, self.colour_3], [self.x, self.y, self.width, self.height])
            
def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    my_list = []
 
    for i in range(1000):
        my_object = Rectangle()
        my_object.x = random.randrange(0,700)
        my_object.y = random.randrange(0,500)
        my_object.change_x = random.randrange(1,5)
        my_object.change_y = random.randrange(1,5)
        my_object.width = random.randrange(1,50)
        my_object.height = random.randrange(1,50)
        my_object.colour_1 = random.randrange(0,256)
        my_object.colour_2 = random.randrange(0,256)
        my_object.colour_3 = random.randrange(0,256)
        
        my_list.append(my_object)
        
    for i in range(1000):
        my_ellipse = Ellipse()
        my_ellipse.x = random.randrange(0,700)
        my_ellipse.y = random.randrange(0,500)
        my_ellipse.change_x = random.randrange(1,5)
        my_ellipse.change_y = random.randrange(1,5)
        my_ellipse.width = random.randrange(1,50)
        my_ellipse.height = random.randrange(1,50)
        my_ellipse.colour_1 = random.randrange(0,256)
        my_ellipse.colour_2 = random.randrange(0,256)
        my_ellipse.colour_3 = random.randrange(0,256)
        
        my_list.append(my_ellipse)    
    
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        for j in range(len(my_list)):
            #my_list[j].move()
            my_list[j].draw(screen)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()