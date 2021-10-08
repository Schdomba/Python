class GUI:
    def __init__(self, width = 1000, height = 1000):
        self.display_width = width
        self.display_height = height
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption('Sudoku')

        self.sd = 0 #an instance of sudoku
        self.subsecSize = 0 #width or height of a subsection (in tiles)
        self.boardSize = 0 #width or height of the board (in tiles)

        self.tilePos = [] #list of tile positions (top left corner)

        self.largeText = pygame.font.Font('freesansbold.ttf',50)
        self.mediumText = pygame.font.Font('freesansbold.ttf', 25)
        self.smallText = pygame.font.Font('freesansbold.ttf', 15)

        self.black = (0,0,0)
        self.grey = (200,200,200)
        self.white = (255,255,255)
        self.red = (255,0,0)
    
        self.clock = pygame.time.Clock()
    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
        
    def game_intro(self):
        #create the text for the game options
        optionsStr = ("4x4", "9x9", "16x16")
        options = []
        options.append(list(self.text_objects(optionsStr[0], self.mediumText, self.grey)) + [2])
        options.append(list(self.text_objects(optionsStr[1], self.mediumText, self.grey)) + [3])
        options.append(list(self.text_objects(optionsStr[2], self.mediumText, self.grey)) + [4])

        #list of blitted option texts (needed for collision detection)
        blitOptions = []
        for opt in options:
            blitOptions.append(self.gameDisplay.blit(opt[0], opt[1]))

        #variable to break the intro loop
        intro = True

        #intro loop
        while intro:
            #always refresh the display in the beginning                
            self.gameDisplay.fill(self.white)
            #create a large text
            TextSurf, TextRect = self.text_objects("Sudoku", self.largeText, self.black)
            #center the text
            TextRect.center = ((self.display_width/2),(self.display_height/2))
            #blit the text
            self.gameDisplay.blit(TextSurf, TextRect)
            
            #paint the option black, if mouse hovers over it, otherwise paint it grey
            pos = pygame.mouse.get_pos()
            i = 0
            for opt in blitOptions:
                if opt.collidepoint(pos):
                    options[i][0], options[i][1] = self.text_objects(optionsStr[i], self.mediumText, self.black)
                else:
                    options[i][0], options[i][1] = self.text_objects(optionsStr[i], self.mediumText, self.grey)
                i+=1
            #position the option texts on the screen
            for i in range(3):
                options[i][1].center = (((i+1)*self.display_width/4),(6*self.display_height/8))
            
            #refresh the list of blitted options
            for i in range(len(blitOptions)):
                blitOptions[i] = self.gameDisplay.blit(options[i][0], options[i][1])

            #check the events
            for event in pygame.event.get():        
                #if option was clicked, create Sudoku and end intro loop        
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 is left mouse button
                    pos = pygame.mouse.get_pos()
                    i = 0
                    for opt in blitOptions:
                        if opt.collidepoint(pos):
                            self.sd = Sudoku(options[i][2])
                            intro = False
                        i+=1
                #quit the game on quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(30)
            
    def drawLines(self):
        #position of thick line (between subsections)
        thickPosx = 0
        thickPosy = 0
        #outer loop for thick lines
        for i in range(1, self.subsecSize+1):
            #inner loop for thin lines
            for j in range (1, self.subsecSize):
                #draw thin lines
                pygame.draw.line(self.gameDisplay,self.black,(thickPosx+j*self.display_width/self.boardSize,0),(thickPosx+j*self.display_width/self.boardSize,self.display_height))
                pygame.draw.line(self.gameDisplay,self.black,(0,thickPosy+j*self.display_height/self.boardSize),(self.display_width,thickPosy+j*self.display_height/self.boardSize))
            #don't draw thick line in last iteration
            if(i==self.subsecSize):
                break
            #next position of thick lines
            thickPosx = i*self.display_width/self.subsecSize
            thickPosy = i*self.display_height/self.subsecSize
            #draw thick lines
            pygame.draw.line(self.gameDisplay,self.black,(thickPosx,0),(thickPosx,self.display_height),4)
            pygame.draw.line(self.gameDisplay,self.black,(0,thickPosy),(self.display_width,thickPosy),4)

    def drawTilePossib(self, possib, pos):
        possib_width = self.display_width/(self.boardSize*self.subsecSize)
        possib_height = self.display_height/(self.boardSize*self.subsecSize)
        xoffset = pos[0]+possib_width/2
        yoffset = pos[1]+possib_height/2
        blitted = []

        for i in range(1, self.subsecSize+1):
            for j in range(self.subsecSize):
                if (i+self.subsecSize*j) in possib:
                    temp = list(self.text_objects(str(i+self.subsecSize*j), self.mediumText, self.grey))
                    temp[1].center = (((i-1)*possib_height+yoffset),(j*possib_width+xoffset))
                    blitted.append(self.gameDisplay.blit(temp[0], temp[1]))
        return blitted
                
    def drawPossib(self):
        blitted = []
        possib = self.sd.getPossib()
        for i in range(len(self.tilePos)):
            blitted.append(self.drawTilePossib(possib[i], self.tilePos[i]))
        return blitted

    def drawTileValues(self):
        tileWidth = self.display_width/self.boardSize
        tileHeight = self.display_height/self.boardSize
        xoffset = tileWidth/2
        yoffset = tileHeight/2
        blitted = []
        values = self.sd.getBoard()
        fixed = self.sd.getFixed()
        color = self.black

        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j] != 0:
                    if fixed[i][j] is True:
                        color = self.red
                    else:
                        color = self.black
                    temp = list(self.text_objects(str(values[i][j]), self.largeText, color))
                    temp[1].center = ((j*tileWidth+xoffset), (i*tileHeight+yoffset))
                    blitted.append(self.gameDisplay.blit(temp[0], temp[1]))
        return blitted
        
    def calcPos(self, pos):
        tileWidth = self.display_width/self.boardSize
        tileHeight = self.display_height/self.boardSize
        possibWidth = self.display_width/(self.boardSize*self.subsecSize)
        possibHeight = self.display_height/(self.boardSize*self.subsecSize)

        #calculate which subsec row the tile is in
        subsecRow = math.floor(pos[1]/(tileHeight*self.subsecSize))
        #calculate which subsec column the tile is in
        subsecCol = math.floor(pos[0]/(tileWidth*self.subsecSize))
        #calculate which row inside of subsec
        row = math.floor((pos[1] - subsecRow*tileHeight*self.subsecSize)/tileHeight)
        #calculate which column inside of subsec
        col = math.floor((pos[0] - subsecCol*tileWidth*self.subsecSize)/tileWidth)

        #calculate which column inside this tile the possib is
        possibCol = math.floor((pos[0] - subsecCol*tileWidth*self.subsecSize - col*tileWidth)/possibWidth)
        #calculate which row inside this tile the possib is
        possibRow = math.floor((pos[1] - subsecRow*tileHeight*self.subsecSize - row*tileHeight)/possibHeight)
        #calculate which possib has been clicked based on col and row
        possib = round(possibRow * self.subsecSize + possibCol + 1)
        
        return(list([subsecRow] + [subsecCol] + [row] + [col] + [possib]))

    def game_loop(self):
        #print("in game_loop")
        #print(self.sd.getBoard())
        #self.sd.writeTile(0,0,0,0,1,True)
        self.subsecSize = self.sd.size
        self.boardSize = self.subsecSize*self.subsecSize
        self.tilePos = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.tilePos.append([i*self.display_width/self.boardSize, j*self.display_height/self.boardSize])
        #print(tilePos)

        gameExit = False
        
        while not gameExit:
            #always refresh the display in the beginning                
            self.gameDisplay.fill(self.white)
            self.drawLines()
            self.drawPossib()
            self.drawTileValues()
            #get the length of board, get the square root to get height/width
            #create rectangles in a loop
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 is left mouse button
                    #check where the player clicked
                    pos = pygame.mouse.get_pos()
                    #calculate which tile and possible value that corresponds to
                    possib = self.calcPos(pos)
                    #if player clicked on possible, write that to the tile
                    if not self.sd.writeTile(possib[0],possib[1],possib[2],possib[3],possib[4]):
                        #if tile already has a value, delete it
                        self.sd.clearTile(possib[0],possib[1],possib[2],possib[3])
                
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #3 is right mouse button
                    #check where the player clicked
                    pos = pygame.mouse.get_pos()
                    #calculate which tile and possible value that corresponds to
                    possib = self.calcPos(pos)
                    #if player clicked on possible, write that to the tile as fixed Tile
                    if not self.sd.writeTile(possib[0],possib[1],possib[2],possib[3],possib[4],True):
                        #if tile already has a value, delete it
                        self.sd.clearTile(possib[0],possib[1],possib[2],possib[3])

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    solver = Solver(self.sd)
                    self.sd = solver.solveNextTile()

            pygame.display.update()
            if self.sd.checkWin():
                break
            #fixed framerate
            self.clock.tick(60)

    def winscreen(self):
        gameExit = False

        while not gameExit:            
            self.gameDisplay.fill(self.white)
            temp = list(self.text_objects("Congratulations, you have won!", self.largeText, self.black))
            temp[1].center = (self.display_width/2, self.display_height/2)
            self.gameDisplay.blit(temp[0], temp[1])

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 is left mouse button
                    gameExit = True


            pygame.display.update()
            #fixed framerate
            self.clock.tick(60)


if __name__ == "__main__":
    import pygame
    from sudoku import Sudoku
    import math
    from makeSudoku import Solver

    pygame.init()   
    theGame = GUI()
    while True:
        theGame.game_intro()
        theGame.game_loop()
        theGame.winscreen()
    pygame.quit()
    quit()