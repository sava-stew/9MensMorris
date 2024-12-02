from Board import Board
from SetUp import SetUp

if __name__ == "__main__":
    setUp = SetUp()
    setUp.setUpWindow()


    if setUp.game_type is not None:
        board = Board(setUp, game_type=setUp.game_type)
        board.setUp()
        board.mainloop()
    else:
        print("No game type selected.")
