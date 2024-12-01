from Board import Board
from SetUp import SetUp

if __name__=="__main__":
    setUp = SetUp()
    setUp.setUpWindow()
    board = Board(setUp)
    board.setUp()
    board.mainloop()