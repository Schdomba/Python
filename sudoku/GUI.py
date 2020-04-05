import pygame
import time
import random
from sudoku import Sudoku

pygame.init()
 
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sudoku')

sd = 0 #an instance of sudoku
subsecSize = 0 #width or height of a subsection (in tiles)
boardSize = 0 #width or height of the board (in tiles)

tilePos = [] #list of tile positions (top left corner)

largeText = pygame.font.Font('freesansbold.ttf',50)
mediumText = pygame.font.Font('freesansbold.ttf', 25)
smallText = pygame.font.Font('freesansbold.ttf', 15)

black = (0,0,0)
grey = (200,200,200)
white = (255,255,255)
red = (255,0,0)
 
clock = pygame.time.Clock()
 
 
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    

def game_intro():
    #create the text for the game options
    optionsStr = ("4x4", "9x9", "16x16")
    options = []
    options.append(list(text_objects(optionsStr[0], mediumText, grey)) + [2])
    options.append(list(text_objects(optionsStr[1], mediumText, grey)) + [3])
    options.append(list(text_objects(optionsStr[2], mediumText, grey)) + [4])

    #list of blitted option texts (needed for collision detection)
    blitOptions = []
    for opt in options:
        blitOptions.append(gameDisplay.blit(opt[0], opt[1]))

    #variable to break the intro loop
    intro = True

    #intro loop
    while intro:
        #always refresh the display in the beginning                
        gameDisplay.fill(white)
        #create a large text
        TextSurf, TextRect = text_objects("Sudoku", largeText, black)
        #center the text
        TextRect.center = ((display_width/2),(display_height/2))
        #blit the text
        gameDisplay.blit(TextSurf, TextRect)
        
        #paint the option black, if mouse hovers over it, otherwise paint it grey
        pos = pygame.mouse.get_pos()
        i = 0
        for opt in blitOptions:
            if opt.collidepoint(pos):
                options[i][0], options[i][1] = text_objects(optionsStr[i], mediumText, black)
            else:
                options[i][0], options[i][1] = text_objects(optionsStr[i], mediumText, grey)
            i+=1
        #position the option texts on the screen
        for i in range(3):
            options[i][1].center = (((i+1)*display_width/4),(6*display_height/8))
        
        #refresh the list of blitted options
        for i in range(len(blitOptions)):
            blitOptions[i] = gameDisplay.blit(options[i][0], options[i][1])

        #check the events
        for event in pygame.event.get():        
            #if option was clicked, create Sudoku and end intro loop        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 is left mouse button
                pos = pygame.mouse.get_pos()
                i = 0
                for opt in blitOptions:
                    if opt.collidepoint(pos):
                        global sd
                        sd = Sudoku(options[i][2])
                        intro = False
                    i+=1
            #quit the game on quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(15)
        
def drawLines():
    #position of thick line (between subsections)
    thickPosx = 0
    thickPosy = 0
    #outer loop for thick lines
    for i in range(1, subsecSize+1):
        #inner loop for thin lines
        for j in range (1, subsecSize):
            #draw thin lines
            pygame.draw.line(gameDisplay,black,(thickPosx+j*display_width/boardSize,0),(thickPosx+j*display_width/boardSize,display_height))
            pygame.draw.line(gameDisplay,black,(0,thickPosy+j*display_height/boardSize),(display_width,thickPosy+j*display_height/boardSize))
        #don't draw thick line in last iteration
        if(i==subsecSize):
            break
        #next position of thick lines
        thickPosx = i*display_width/subsecSize
        thickPosy = i*display_height/subsecSize
        #draw thick lines
        pygame.draw.line(gameDisplay,black,(thickPosx,0),(thickPosx,display_height),4)
        pygame.draw.line(gameDisplay,black,(0,thickPosy),(display_width,thickPosy),4)


def drawTilePossib(possib, pos):
    possib_width = display_width/(boardSize*subsecSize)
    possib_height = display_height/(boardSize*subsecSize)
    xoffset = pos[0]+possib_width/2
    yoffset = pos[1]+possib_height/2
    blitted = []

    for i in range(1, subsecSize+1):
        for j in range(subsecSize):
            if (i+subsecSize*j) in possib:
                temp = list(text_objects(str(i+subsecSize*j), smallText, grey)) + [i+subsecSize*j]
                temp[1].center = (((i-1)*possib_width+xoffset), (j*possib_height+yoffset))
                blitted.append(gameDisplay.blit(temp[0], temp[1]))
    return blitted
               
def drawPossib():
    possib = sd.getPossib()
    for i in range(len(tilePos)):
        drawTilePossib(possib[i], tilePos[i])
    
#TBD!
def game_loop():
    print("in game_loop")
    print(sd.getBoard())
    sd.writeTile(0,0,0,0,1)
    print(sd.getBoard())
    global subsecSize
    global boardSize
    global tilePos
    subsecSize = sd.size
    boardSize = subsecSize*subsecSize
    for i in range(boardSize):
        for j in range(boardSize):
            tilePos.append([i*display_width/boardSize, j*display_height/boardSize])
    print(tilePos)

    gameExit = False
    
    while not gameExit:
        #always refresh the display in the beginning                
        gameDisplay.fill(white)
        drawLines()
        drawPossib()
        #get the length of board, get the square root to get height/width
        #create rectangles in a loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 is left mouse button
                break
                #check which tile has been clicked
                #mark this tile
                #let the player enter a number
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()