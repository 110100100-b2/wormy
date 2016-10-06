x = 200
y = 50

import pygame
from random import randint

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
 
# Define some colors
BLACK = (0, 0, 0)
GRAY = (61, 65, 71)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#GLOBALS
length = 0 #length of snake
current_direction = 'right'
score = 0
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 2
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(30):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(30):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[y][x] = (x, y)
snakeCoords = [{'x': 15,     'y': 15}, #Head
               {'x': 15 - 1, 'y': 15},
               {'x': 15 - 2, 'y': 15}] #Tail

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [660, 660]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Wormy")
 
# Loop until the user clicks the close button.
done = False

def updateGrid(x,y, grid):
    grid[y][x] = 0

def moveSnake(grid, direction, snakeCoords):
    if (direction == 'right'):
        if (snakeCoords[0]['x'] < 29):
            snakeCoords.insert(0, {'x': snakeCoords[0]['x']+1, 'y':snakeCoords[0]['y']}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass
            else:    
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)                
                del snakeCoords[-1]            
            
            
            
    elif(direction == 'left'):
        if (snakeCoords[0]['x'] >= 1):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x']-1, 'y':snakeCoords[0]['y']}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass            
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1] 
    elif(direction == 'up'):
        if (snakeCoords[0]['y'] >= 1):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x'], 'y':snakeCoords[0]['y']-1}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass            
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1]

    elif(direction == 'down'):
        if (snakeCoords[0]['y'] < 29):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x'], 'y':snakeCoords[0]['y']+1}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass 
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1] 


def drawSnake(snakeCoords, grid):
    for i in range(len(snakeCoords)):
        x = snakeCoords[i]['x']
        y = snakeCoords[i]['y']
        grid[y][x] = 1
        
        
def drawGrid(grid):
    global BLACK
    global RED
    global MARGIN
    global WIDTH
    global HEIGHT
    for row in range(30):
        for column in range(30):
            color = BLACK
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED                   
            pygame.draw.rect(screen, color,
                             [50+(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT]) 

def createApple(grid):
    rand_x = randint(0,29)
    rand_y = randint(0,29)
    grid[rand_y][rand_x] = 2
    return [rand_x, rand_y]

apple = createApple(grid)
            
def ateApple(grid, snakeCoords):
    global apple
    global score
    global current_direction
    if (snakeCoords[0]['x'] == apple[0] and snakeCoords[0]['y'] == apple[1]):
        grid[apple[1]][apple[0]] = 0
        score += 1
        print('Hello WOrld')
        apple = createApple(grid)
        return True
    else:
        return False
            
        
   

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and current_direction != 'down':
                current_direction = 'up'
                pass
            elif event.key == pygame.K_DOWN and current_direction != 'up':
                current_direction = 'down'
                pass
            elif event.key == pygame.K_LEFT and current_direction != 'right':
                current_direction = 'left'
                pass
            elif event.key == pygame.K_RIGHT and current_direction != 'left':
                current_direction = 'right'
                pass
 
    # Set the screen background
    screen.fill(GRAY)    
    
    #Move and draw the snake
    moveSnake(grid, current_direction, snakeCoords)
    drawSnake(snakeCoords, grid)
 
    # Draw the grid
    drawGrid(grid)
 
    # Limit to 15 frames per second
    clock.tick(15)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()


