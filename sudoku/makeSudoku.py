class Solver:
    def __init__(self, sd):
        self.sd = sd

    def solveNextTile(self):
        #check for tile with the least number of possible values
        board = self.sd.board.board
        size = self.sd.board.size

        lowestSubsecRow = 0
        lowestSubsecCol = 0
        lowestRow = 0
        lowestCol = 0

        for subsecRow in range(self.sd.board.size):
            for subsecCol in range(self.sd.board.size):
                for row in range(self.sd.board.size):
                    for col in range(self.sd.board.size):
                        #find starting tile
                        if self.sd.board.board[lowestSubsecRow][lowestSubsecCol][lowestRow][lowestCol].hasValue:
                            lowestSubsecRow = subsecRow
                            lowestSubsecCol = subsecCol
                            lowestRow = row
                            lowestCol = col
                        #compare currently lowest tile with all the others
                        elif (not self.sd.board.board[subsecRow][subsecCol][row][col].hasValue) \
                            and len(self.sd.board.board[subsecRow][subsecCol][row][col].possib) < len(self.sd.board.board[lowestSubsecRow][lowestSubsecCol][lowestRow][lowestCol].possib) \
                            and len(self.sd.board.board[subsecRow][subsecCol][row][col].possib) > 0:
                            print("in elif statement")
                            lowestSubsecRow = subsecRow
                            lowestSubsecCol = subsecCol
                            lowestRow = row
                            lowestCol = col
                        
                        else:
                            print("in else statement")
                            print(str(subsecRow) + str(subsecCol) + str(row) + str(col))
                            print(self.sd.board.board[subsecRow][subsecCol][row][col].numOfPossib)

                            print(str(lowestSubsecRow) + str(lowestSubsecCol) + str(lowestRow) + str(lowestCol))
                            print(self.sd.board.board[lowestSubsecRow][lowestSubsecCol][lowestRow][lowestCol].numOfPossib)
        
        possib = self.sd.board.board[lowestSubsecRow][lowestSubsecCol][lowestRow][lowestCol].possib
        #choose one of the possibles and write that to the tile (random or lowest?)
        if len(possib) > 0:
            self.sd.writeTile(lowestSubsecRow, lowestSubsecCol, lowestRow, lowestCol, possib[0])
        return self.sd