class Tile:
    def __init__(self, size):
        self.possib = list(range(1,size+1))
        self.Value = 0
        self.hasValue = False
        self.numOfPossib = size
    def delPossib(self,value):
        if value in self.possib:
            self.possib.remove(value)
            self.numOfPossib -= 1
            return True
        else:
            return False
    def addPossib(self,value):
        if not (value in self.possib):
            self.possib.add(value)
            self.numOfPossib += 1
            return True
        else:
            return False
    def setValue(self,value):
        if value in self.possib:
            self.value = value
            self.hasValue = True
            self.possib.clear()
            self.numOfPossib = 0
            return True
        else:
            return False
            
    def clearValue(self):
        value = self.Value
        self.possib.add(value)
        self.Value = 0
        self.hasvalue = False
        return value
    