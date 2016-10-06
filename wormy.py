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
game_state = 0
 
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


def randomStartingPosition():
    return [randint(2,29), randint(0, 29)]

#grid[y][x] = (x, y)

startingPosition = randomStartingPosition()
snakeCoords = [{'x': startingPosition[0],     'y': startingPosition[0]}, #Head
               {'x': startingPosition[0]- 1,  'y': startingPosition[0]},
               {'x': startingPosition[0]- 2,  'y': startingPosition[0]}] #Tail

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


def moveSnake(grid, direction, snakeCoords, screen):
    global game_state
    if (direction == 'right'):
        if (snakeCoords[0]['x'] < 29):
            snakeCoords.insert(0, {'x': snakeCoords[0]['x']+1, 'y':snakeCoords[0]['y']}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass
            elif(ateSelf(grid, snakeCoords)):
                pass
            else:    
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)                
                del snakeCoords[-1]            
        else:
            gameOver(screen)
            game_state = 1
            
            
            
    elif(direction == 'left'):
        if (snakeCoords[0]['x'] >= 1):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x']-1, 'y':snakeCoords[0]['y']}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass
            elif(ateSelf(grid, snakeCoords)):
                pass            
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1]
        else:
            gameOver(screen)
            game_state = 1
    elif(direction == 'up'):
        if (snakeCoords[0]['y'] >= 1):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x'], 'y':snakeCoords[0]['y']-1}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass
            elif(ateSelf(grid, snakeCoords)):
                pass            
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1]
        else:
            gameOver(screen)
            game_state = 1

    elif(direction == 'down'):
        if (snakeCoords[0]['y'] < 29):            
            snakeCoords.insert(0, {'x': snakeCoords[0]['x'], 'y':snakeCoords[0]['y']+1}) #Adding new head
            if (ateApple(grid, snakeCoords)):
                pass
            elif(ateSelf(grid, snakeCoords)):
                pass            
            else:
                updateGrid(snakeCoords[-1]['x'], snakeCoords[-1]['y'], grid)
                del snakeCoords[-1] 
        else:
            gameOver(screen)
            game_state = 1

def drawSnake(snakeCoords, grid):
    for i in range(len(snakeCoords)):
        x = snakeCoords[i]['x']
        y = snakeCoords[i]['y']
        grid[y][x] = 1
        


def gameOver(screen):
    h1 = pygame.font.SysFont("monospace", 36)
    h3 = pygame.font.SysFont("monospace", 15)
    # render text
    game_over = h1.render("Game Over!", 1, (255,255,0))
    play_again = h3.render("Press 'r' to play again.", 1, (255,255,0))
    screen.blit(game_over, (240, 100))
    screen.blit(play_again, (240, 500)) 

        
        
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
                             [(MARGIN + WIDTH) * column + MARGIN,
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
        print('Score is {}'.format(score))
        apple = createApple(grid)
        return True
    else:
        return False

def ateSelf(grid, snakeCoords):
    global score
    #score -= length of deleted parts
    head = snakeCoords[0]
    for i in range(1, len(snakeCoords)):
        if (head == snakeCoords[i]): #Snake bit itself
            remaining_snake = snakeCoords[:i]
            bit_off_part = snakeCoords[i+1:]
            score -= len(bit_off_part)
            snakeCoords = remaining_snake
            for j in range(len(bit_off_part)): #Zeroing out entries of bit_off_part
                x = bit_off_part[j]['x']
                y = bit_off_part[j]['y']
                grid[y][x] = 0
            return True  
    return False      
        
def reset():
    global score
    global grid
    global apple
    global snakeCoords
    for i in range(30):
        for j in range(30):
            grid[i][j] = 0
    apple = createApple(grid)
    score = 0
    startingPosition = randomStartingPosition()
    snakeCoords = [{'x': startingPosition[0],     'y': startingPosition[0]}, #Head
               {'x': startingPosition[0]- 1,  'y': startingPosition[0]},
               {'x': startingPosition[0]- 2,  'y': startingPosition[0]}] #Tail   
    
     

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and current_direction != 'down' and game_state == 0:
                current_direction = 'up'
                pass
            elif event.key == pygame.K_DOWN and current_direction != 'up' and game_state == 0:
                current_direction = 'down'
                pass
            elif event.key == pygame.K_LEFT and current_direction != 'right' and game_state == 0:
                current_direction = 'left'
                pass
            elif event.key == pygame.K_RIGHT and current_direction != 'left' and game_state == 0:
                current_direction = 'right'
                pass
            if event.key == pygame.K_r and game_state == 1:
                reset()
                game_state = 0
                
 
    # Set the screen background
    screen.fill(GRAY)    
    
    
 
    # Draw the grid
    drawGrid(grid)
    
    #Move and draw the snake
    moveSnake(grid, current_direction, snakeCoords, screen)
    drawSnake(snakeCoords, grid)    
 
    # Limit to 15 frames per second
    clock.tick(15)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()


