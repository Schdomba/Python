from board import Board

class Sudoku:
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
    
    def getBoard(self):
        tmpRow = []
        output = []
        printOutput = ""
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        tmpRow.append(self.board.getTileVal(subsecRow, subsecCol, row, col))
                        printOutput += str(self.board.getTileVal(subsecRow, subsecCol, row, col))
                    printOutput += "|"
                output.append(tmpRow)
                tmpRow = []
                printOutput += "\n"
            printOutput += "--------\n"
        print(printOutput)
        return output

    def getEmpty(self):
        output = []
        i = 0
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        if not self.board.getTileHasValue(subsecRow, subsecCol, row, col):
                            output.append([])
                            output[i].append(subsecRow)
                            output[i].append(subsecCol)
                            output[i].append(row)
                            output[i].append(col)       
                            i += 1
        return output

    def getPossib(self):
        output = []
        i = 0
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        output.append(self.board.getTilePossib(subsecRow, subsecCol, row, col))     
                        i += 1 
        return output
    
    def getFixed(self):
        output = []
        tmpRow = []
        for subsecRow in range(self.size):
            for row in range(self.size):
                for subsecCol in range(self.size):
                    for col in range(self.size):
                        tmpRow.append(self.board.getTileFixed(subsecRow, subsecCol, row, col))
                output.append(tmpRow)
                tmpRow = []
        return output

    def writeTile(self, subsecRow, subsecCol, row, col, value, fix=False):
        return self.board.writeTile(subsecRow, subsecCol, row, col, value, fix)

    def clearTile(self, subsecRow, subsecCol, row, col):
        return self.board.clearTile(subsecRow, subsecCol, row, col)     

    def checkWin(self):
        if (len(self.getEmpty()) > 0):
            return False
        else:
            return True
            