# author: Yannik Stumpp
# date: 21.03.2020

from tile import Tile
class Board:
    #================================================================================
    # short: this function is the init function
    #--------------------------------------------------------------------------------
    # long:
    #   this function initializes the class. The class contains:
    #   size: the size of one subsection of the sudoku board
    #   board: a 4D array representing the sudoku board, consisting of size*size
    #          subsections (standard: 9). Every subsection contains size*size tiles.
    #   
    # 
    #   subsec|subsec|subsec
    #   --------------------
    #   subsec|subsec|subsec    <-- board (size = 3) with size*size subsections
    #   --------------------        addressing: [subsecRow][subsecCol]
    #   subsec|subsec|subsec
    #                  / \
    #                 /   \
    #                 _____
    #                |1 2 3|
    #                |4 5 6|    <-- subsection (size = 3) with size*size tiles
    #                |7 8 9|        addressing: [row][col]
    #                 ¯¯¯¯¯
    #   
    # paramters:
    #   size: the width and height of one subsection
    #================================================================================
    def __init__(self, size=3):
        self.size = size
        #create a board, made out of size*size subsections 
        #(3x3 subsections or 9x9 tiles is standard sudoku)
        #a board is a 4D array [subsecRow][subsecCol][row][col]
        self.board = []
        for subsecRow in range(self.size):
            self.board.append([])
            for subsecCol in range(self.size):
                self.board[subsecRow].append([])
                for row in range(self.size):
                    self.board[subsecRow][subsecCol].append([])
                    for col in range(self.size):
                        self.board[subsecRow][subsecCol][row].append(Tile(self.size*self.size))

    #================================================================================
    # short: this function returns affected tiles
    #--------------------------------------------------------------------------------
    # long:
    #   If the value of a tile changes, every tile in the same row, column or
    #   subsection is affected by this change. This function returns them.
    # paramters:
    #   subsecRow: row in which the subsection containing the tile is located
    #   subsecCol: column in which the subsection containing the tile is located
    #   row: row inside the subsection in which the tile is located
    #   col: column inside the subsection in which the tile is located
    # return: Tile[]
    #   a list of tiles, affected by the change
    #================================================================================
    def giveAffectedTiles(self, subsecRow, subsecCol, row, col):
        affectedTiles = []
        for i in range(self.size):
            for j in range (self.size):
                # every tile in the same row
                if self.board[subsecRow][i][row][j] not in affectedTiles:
                    affectedTiles.append(self.board[subsecRow][i][row][j])
                # every tile in the same column
                if self.board[i][subsecCol][j][col] not in affectedTiles:
                    affectedTiles.append(self.board[i][subsecCol][j][col])
                # every tile in the same subsection
                if self.board[subsecRow][subsecCol][i][j] not in affectedTiles:
                    affectedTiles.append(self.board[subsecRow][subsecCol][i][j])
        return affectedTiles

    #================================================================================
    # short: this function returns the position of affected tiles
    #--------------------------------------------------------------------------------
    # long:
    #   If the value of a tile changes, every tile in the same row, column or
    #   subsection is affected by this change. THis function returns their
    #   positions on the board.
    # paramters:
    #   subsecRow: row in which the subsection containing the tile is located
    #   subsecCol: column in which the subsection containing the tile is located
    #   row: row inside the subsection in which the tile is located
    #   col: column inside the subsection in which the tile is located
    # return: list
    #   a list of tile positions. each Element has the structure
    #   [subsecRow, subsecCol, row, col]
    #================================================================================
    def giveAffectedPos(self, subsecRow, subsecCol, row, col):
        affectedPos = []
        for i in range(self.size):
            for j in range (self.size):
                # every tile in the same row
                if [subsecRow, i, row, j] not in affectedPos:
                    affectedPos.append([subsecRow, i, row, j])
                # every tile in the same column
                if [i, subsecCol, j, col] not in affectedPos:
                    affectedPos.append([i, subsecCol, j, col])
                # every tile in the same subsection
                if [subsecRow, subsecCol, i, j] not in affectedPos:
                    affectedPos.append([subsecRow, subsecCol, i, j])
        return affectedPos

    #================================================================================
    # short: this function tries to write a given value to a specified tile
    #--------------------------------------------------------------------------------
    # long: 
    #   If the tile already contains a value or this value is not in the tiles 
    #   list of possible values, the value won't be written to the tile.
    #   If the value was written to the tile, every affected tile (same row,
    #   column or subsection) gets updated.
    # paramters:
    #   subsecRow: row in which the subsection containing the tile is located
    #   subsecCol: column in which the subsection containing the tile is located
    #   row: row inside the subsection in which the tile is located
    #   col: column inside the subsection in which the tile is located
    #   value: value that has to be written to the tile
    # return: boolean
    #   True: the value was succesfully written to the tile
    #   False: this value cannot be written to the specified tile
    #================================================================================
    def writeTile(self, subsecRow, subsecCol, row, col, value):
        theTile = self.board[subsecRow][subsecCol][row][col]
        if theTile.hasValue:
            return False
        elif value in theTile.possib:
            theTile.setValue(value)
            # delete possible value from every affected tile
            for elem in self.giveAffectedTiles(subsecRow, subsecCol, row, col):
                elem.delPossib(value)
            return True
        else:
            return False
    
    #================================================================================
    # short: this function clears the value of a tile
    #--------------------------------------------------------------------------------
    # long: 
    #   If the tile contains a value, it will be cleared. The function checks 
    #   every affected tile (same row, column or subsection) afterwards and adds
    #   the value to the list of possible values if necessary.
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
        theTile = self.board[subsecRow][subsecCol][row][col]
        # if tile has no value it cannot be cleared
        if not theTile.hasValue:
            return False
        # if tile has value, clear it and update all the affected tiles
        else:
            value = theTile.clearValue()
            if value == 0:
                return False
            else:
                affectedTiles = self.giveAffectedTiles(subsecRow, subsecCol, row, col)
                # this tile cannot have Values already in the affectedTiles
                for elem in affectedTiles:
                    if elem.hasValue:
                        theTile.delPossib(elem.value)
                
                # positions affected by this tile
                affectedPos = self.giveAffectedPos(subsecRow, subsecCol, row, col)
                # for every affected position
                for pos in affectedPos:
                    isPossible = True
                    # check same row, column and subsection
                    for elem in self.giveAffectedTiles(pos[0], pos[1], pos[2], pos[3]):
                        # if the value is anywhere in the same row, column or subsection,
                        # end this loop
                        if elem.value == value:
                            isPossible = False
                            break
                    # if the value wasn't anywhere in the same row, column or subsection,
                    # add it to the possible values
                    if isPossible:
                        self.board[pos[0]][pos[1]][pos[2]][pos[3]].addPossib(value)
                return True