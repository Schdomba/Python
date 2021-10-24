from board import Board

class Sudoku:
    #================================================================================
    # short: this function is the init function
    #--------------------------------------------------------------------------------
    # long:
    #   this function initializes the class. The class contains:
    #   size: the size of one subsection of the sudoku board
    #   board: an instance of Board with the corresponding size
    # paramters:
    #   size: the width and height of one subsection
    #================================================================================
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
    
    #================================================================================
    # short: this function returns a representation of board
    #--------------------------------------------------------------------------------
    # long:
    #   the list represents rows and cols, no subsections. This reduces complexity
    #   and dimensions from 4 to 2.
    #   The list is accessed as [row][col].
    # paramters:
    #   none
    # return: int[][]
    #   a 2 dimensional list of tile values
    #================================================================================
    def getBoard(self):
        output = [ [ self.board.getTileVal(subsecRow, subsecCol, row, col) for subsecCol in range(self.size) for col in range(self.size) ] \
                for subsecRow in range(self.size) for row in range(self.size) ]
        return output
    
    #================================================================================
    # short: this function returns a list of empty tile positions
    #--------------------------------------------------------------------------------
    # long:
    #   Each entry of the list represents an empty tile position and looks like:
    #   [subsecRow, subsecCol, row, col].
    #   The number of entries in this list is the number of empty tiles.
    # paramters:
    #   none
    # return: int[][]
    #   a 2 dimensional list of empty tile positions
    #================================================================================
    def getEmpty(self):
        output = [ [ subsecRow, subsecCol, row, col ] \
                    for subsecRow in range(self.size) for row in range(self.size) for subsecCol in range(self.size) for col in range(self.size)\
                    if not self.board.getTileHasValue(subsecRow, subsecCol, row, col)]
        return output

    #================================================================================
    # short: this function returns a list of possible values
    #--------------------------------------------------------------------------------
    # long:
    #   Each entry of the list is another list of the possible values of one tile.
    #   If a tile has no possible values left, the corresponding entry is an 
    #   empty list.
    # paramters:
    #   none
    # return: int[][]
    #   a 2 dimensional list of tile possible values
    #================================================================================
    def getPossib(self):
        output = [ self.board.getTilePossib(subsecRow, subsecCol, row, col) \
            for subsecRow in range(self.size) for row in range(self.size) \
            for subsecCol in range(self.size) for col in range(self.size) ]
        return output

    #================================================================================
    # short: this function returns a list of tile fixed values
    #--------------------------------------------------------------------------------
    # long:
    #   the list represents rows and cols, no subsections. This reduces complexity
    #   and dimensions from 4 to 2.
    #   The list is accessed as [row][col].
    # paramters:
    #   none
    # return: int[][]
    #   a 2 dimensional list of tile fixed values
    #================================================================================
    def getFixed(self):
        output = [ [ self.board.getTileFixed(subsecRow, subsecCol, row, col) for subsecCol in range(self.size) for col in range(self.size) ] \
                for subsecRow in range(self.size) for row in range(self.size) ]
        return output

    #================================================================================
    # short: this is a wrapper for board.writeTile
    #--------------------------------------------------------------------------------
    # paramters:
    #   subsecRow: row in which the subsection containing the tile is located
    #   subsecCol: column in which the subsection containing the tile is located
    #   row: row inside the subsection in which the tile is located
    #   col: column inside the subsection in which the tile is located
    # return: boolean
    #   True: the value was succesfully written to the tile
    #   False: this value cannot be written to the specified tile
    #================================================================================
    def writeTile(self, subsecRow, subsecCol, row, col, value, fix=False):
        return self.board.writeTile(subsecRow, subsecCol, row, col, value, fix)

    #================================================================================
    # short: this is a wrapper for board.clearTile
    #--------------------------------------------------------------------------------
    # paramters:
    #   subsecRow: row in which the subsection containing the tile is located
    #   subsecCol: column in which the subsection containing the tile is located
    #   row: row inside the subsection in which the tile is located
    #   col: column inside the subsection in which the tile is located
    # return: boolean
    #   True: the tile was successfully cleared
    #   False: the tile cannot be cleared.
    #================================================================================
    def clearTile(self, subsecRow, subsecCol, row, col):
        return self.board.clearTile(subsecRow, subsecCol, row, col)  

    #================================================================================
    # short: this function checks if the game is won
    #--------------------------------------------------------------------------------
    # paramters:
    #   none
    # return: boolean
    #   True: the game is won (all tiles have a value)
    #   False: the game is not won (there are still tiles with no value)
    #================================================================================
    def checkWin(self):
        if (len(self.getEmpty()) > 0):
            return False
        else:
            return True
            