from board import Board

class Sudoku:
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
    
    def giveBoard(self):
        theBoard = self.board.board
        output = ""
        printOutput = ""
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        output += str(theBoard[subsecRow][subsecCol][row][col].value)
                        printOutput += str(theBoard[subsecRow][subsecCol][row][col].value)
                    printOutput += "|"
                printOutput += "\n"
            printOutput += "--------\n"
        print(printOutput)
        return output

    def giveEmpty(self):
        theBoard = self.board.board
        output = []
        i = 0
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        if not theBoard[subsecRow][subsecCol][row][col].hasValue:
                            output.append([])
                            output[i].append(subsecRow)
                            output[i].append(subsecCol)
                            output[i].append(row)
                            output[i].append(col)       
                            i += 1 
        return output

    
    def writeTile(self, subsecRow, subsecCol, row, col, value):
        return self.board.writeTile(subsecRow, subsecCol, row, col, value)
        #check isWon
    
    def clearTile(self, subsecRow, subsecCol, row, col):
        return self.board.clearTile(subsecRow, subsecCol, row, col)
        #check isLost

            

    #def isWon(self):
        #check if game is won
    
    #def isLost(self):
        #check if game is lost