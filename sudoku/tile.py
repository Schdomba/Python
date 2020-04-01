class Tile:
    #================================================================================
    # short: this function is the init function
    #--------------------------------------------------------------------------------
    # long:
    #   this function initializes the class. The class contains:
    #   possib: a list of possible values for this tile
    #   value: the current value of this tile (0 == no value)
    #   hasValue: True, if the tile currently has a value, else false
    #   numOfPossib: the current number of possible values for this tile
    # paramters:
    #   numOfPossib: the maximum number of possible values for this tile
    #================================================================================
    def __init__(self, numOfPossib):
        self.numOfPossib = numOfPossib
        self.possib = list(range(1,self.numOfPossib+1))
        self.value = 0
        self.hasValue = False

    #================================================================================
    # short: this function deletes a possible value from possib
    #--------------------------------------------------------------------------------
    # paramters:
    #   value: the value that has to be deleted
    # return: boolean
    #   True if the value was deleted
    #   False if this value wasn't a possible value
    #================================================================================
    def delPossib(self,value):
        if value in self.possib:
            self.possib.remove(value)
            return True
        else:
            return False

    #================================================================================
    # short: this function adds a possible value to possib
    #--------------------------------------------------------------------------------
    # paramters:
    #   value: the value that has to be added
    # return: boolean
    #   True if the value was added
    #   False if this value is already in possib
    #================================================================================
    def addPossib(self,value):
        if not (value in self.possib):
            self.possib.append(value)
            return True
        else:
            return False

    #================================================================================
    # short: this function sets a tile value
    #--------------------------------------------------------------------------------
    # paramters:
    #   value: the value of the tile
    # return: boolean
    #   True if the value was set
    #   False if this value wasn't a possible value
    #================================================================================
    def setValue(self,value):
        if value in self.possib:
            self.value = value
            self.hasValue = True
            self.possib.clear()
            return True
        else:
            return False
            
    #================================================================================
    # short: this function clears the tiles value
    #--------------------------------------------------------------------------------
    # long:
    #   after clearing the tile, every value is possible again. The board has to
    #   delete the ones that aren't possible.
    # paramters:
    #   none
    # return: number
    #   the value that this tile had before clearing
    #================================================================================
    def clearValue(self):
        if self.value == 0:
            return 0
        else:
            value = self.value
            self.value = 0
            self.hasValue = False
            self.possib = list(range(1,self.numOfPossib+1))
            return value
    