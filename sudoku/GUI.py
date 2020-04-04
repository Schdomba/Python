import pygame
import time
import random
from sudoku import Sudoku

pygame.init()
 
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sudoku')

sd = Sudoku(2) #an instance of sudoku, size changes later

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
        
        
    
    
#TBD!
def game_loop():
    print("in game_loop")
    print(sd.getBoard())

    gameExit = False
    
    while not gameExit:
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
        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()