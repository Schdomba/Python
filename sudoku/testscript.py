from sudoku import Sudoku

sd = Sudoku(2)
#write 4 tiles, get board, get possib, checkWin
sd.writeTile(0,0,0,0,1)
sd.writeTile(0,0,0,1,2)
sd.writeTile(0,0,1,0,3)
sd.writeTile(0,0,1,1,4)
print(sd.getBoard())
print(sd.getPossib())
print(sd.checkWin())

#write and clear a tile, get possib
sd.writeTile(0,1,0,0,3)
sd.clearTile(0,1,0,0)
print(sd.getPossib())

#write every tile, checkWin
sd.writeTile(0,1,0,0,3)
sd.writeTile(0,1,0,1,4)
sd.writeTile(0,1,1,0,1)
sd.writeTile(0,1,1,1,2)

sd.writeTile(1,0,0,0,2)
sd.writeTile(1,0,0,1,1)
sd.writeTile(1,0,1,0,4)
sd.writeTile(1,0,1,1,3)

sd.writeTile(1,1,0,0,4)
sd.writeTile(1,1,0,1,3)
sd.writeTile(1,1,1,0,2)
sd.writeTile(1,1,1,1,1)

print(sd.getBoard())
print(sd.getPossib())
print(sd.checkWin())
