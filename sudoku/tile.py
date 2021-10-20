class Tile:
    #================================================================================
    # short: this function is the init function
    #--------------------------------------------------------------------------------
    # long:
    #   this function initializes the class. The class contains:
    #   __numOfPossib: the maximum number of possible values for this tile
    #   possib: a list of possible values for this tile
    #   value: the current value of this tile (0 == no value)
    #   hasValue: True, if the tile currently has a value, else false
    #   fixed: True, if the tile is set to fixed (value cannot be changed), else false
    # paramters:
    #   numOfPossib: the maximum number of possible values for this tile
    #================================================================================
    def __init__(self, numOfPossib):
        self.__numOfPossib = numOfPossib
        self.possib = list(range(1,self.__numOfPossib+1))
        self.value = 0
        self.hasValue = False
        self.fixed = False
        
        #===========================decorators of self.value=================================
        @property
        def value(self):
            return self.__value
        @value.setter
        def value(self,val):
            #set value if it is in possib, return True
            if val in self.possib:
                self.__value = val
                self.hasValue = True
                del self.possib[:] 
                return True
            #don't set value if it is not in possib, return False
            else:
                return False
        @value.deleter
        def value(self):
            #if Tile has no value, return 0
            if self.__value == 0 or self.fixed is True:
                return 0
            #if Tile has a value, clear it. Reset possib and hasValue, return cleared value
            else:
                val = self.__value
                self.__value = 0
                self.hasValue = False
                self.possib = list(range(1,self.__numOfPossib+1))
                return val

        #===========================decorators of self.fixed=================================
        @property
        def fixed(self):
            return self.__fixed
        @fixed.setter
        def fixed(self, fix):
            if fix is True:
                if self.value == 0 and self.hasValue is False:
                    self.__fixed = False
                    raise RuntimeError("Can't set Tile to fixed because it has no value.")
                else:
                    self.__fixed = True
                    return True
            else:
                if self.fixed is True:
                    raise RuntimeError("Can't unfix a fixed tile.")
                else:
                    self.__fixed = False
                    return True
        @fixed.deleter
        def fixed(self):
            raise RuntimeError("Fixed attribute cannot be deleted.")

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
        if (not (value in self.possib)) and self.hasValue is False:
            self.possib.append(value)
            return True
        else:
            return False
