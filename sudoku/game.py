import tile
class Game:
    def __init__(self, size):
        self.board = []
        self.size = size
        for row in range(self.size*self.size):
            self.board.append([])
            for column in range(self.size*self.size):
                self.board[row].append(tile.Tile(self.size*self.size))
    
    #every board is divided into subsections
    def giveSubsec(self, row, column):
        rowmin = row
        colmin = row
        while(rowmin % self.size != 0):
            rowmin -= 1
        rowmax = rowmin + self.size - 1
        
        while(colmin % self.size != 0):
            colmin -= 1
        colmax = colmin + self.size - 1
        #return first row, last row, first column, last column
        #of this subsection
        subsec = [rowmin, rowmax, colmin, colmax]
        return subsec
    
    def refreshBoard(self, row, column, value):
        # delete this possibility from every tile in the same row
        for obj in self.board[row]:
            obj.delPossib(value)
        # delete this possibility from every tile in the same column
        for i in range(len(self.board)):
            self.board[i][column].delPossib(value)
        # delete this possibility from every tile in the same subsection
        subsec = self.giveSubsec(row, column)
        rowmin = subsec[0]
        rowmax = subsec[1]
        colmin = subsec[2]
        colmax = subsec[3]
        for r in range(rowmin, rowmax):
            for c in range(colmin, colmax):
                self.board[r][c].delPossib(value)
                
    def checkIfPossible(self, row, column, value):
        possible = True
        for obj in self.board[row]
        
    
    def writeTile(self, row, column, value):
        if self.board[row][column].hasValue:
            return False
        elif value in self.board[row][column].possib:
            self.board[row][column].setValue(value)
            self.refreshBoard(row, column, value)
            return True
        else:
            return False
    
    def clearTile(self, row, column)
        value = self.board[row][column].clearValue()
        #check every tile in the same row
        #check every tile in the same column
        #check every tile in the same subsec
    
    def isWon(self):
        for row in range(len(self.board)):
            for obj in self.board[row]:
                if not obj.hasValue:
                    return False
        return True
    
    def isLost(self):
        if self.isWon():
            return False
        else:
            for row in range(len(self.board)):
                for obj in self.board[row]:
                    if not obj.hasValue and len(obj.possib) == 0:
                        return True
        return False