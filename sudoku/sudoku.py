from board import Board

class Sudoku:
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
    
    def getBoard(self):
        theBoard = self.board.board
        tmpRow = []
        output = []
        printOutput = ""
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        tmpRow.append(theBoard[subsecRow][subsecCol][row][col].value)
                        printOutput += str(theBoard[subsecRow][subsecCol][row][col].value)
                    printOutput += "|"
                output.append(tmpRow)
                tmpRow = []
                printOutput += "\n"
            printOutput += "--------\n"
        print(printOutput)
        return output

    def getEmpty(self):
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

    def getPossib(self):
        theBoard = self.board.board
        output = []
        i = 0
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        output.append(theBoard[subsecRow][subsecCol][row][col].possib)     
                        i += 1 
        return output
    
    def writeTile(self, subsecRow, subsecCol, row, col, value):
        return self.board.writeTile(subsecRow, subsecCol, row, col, value)
    
    def clearTile(self, subsecRow, subsecCol, row, col):
        return self.board.clearTile(subsecRow, subsecCol, row, col)

            

    def checkWin(self):
        if (len(self.getEmpty()) > 0):
            return "there are still empty tiles"
        else:
            output = "Congratulations, you have won the game!"
            for elem in self.getPossib():
                if (len(elem) > 0):
                    output = "You have lost the game."
            return output
            