import tkinter as tk
import unittest
from Board import Board, black, white
from GameOver import GameOver
from SetUp import SetUp
from Turn import Turn

setup = SetUp()
#setup.placements = setup.nineMensPlacements
setup.setUpBoard(9)
board = Board(setup)
turn = Turn()
canvas = tk.Canvas()
#placements = setup.nineMensPlacements

class TestMovePiece(unittest.TestCase):

    #def setUp(self):
    #    self.board = Board(SetUp)
    #    self.placements = self.board.placements

    def test_invalid_from_pos(self):
        self.assertNotIn("g2", board.placements)
        self.assertFalse(board.move_piece("g2", "g4"))

    def test_invalid_to_pos(self):
        self.assertNotIn("g3", board.placements)
        self.assertFalse(board.move_piece("g1", "g3"))

    def test_empty_from_pos(self):
        #setup.setUpBoard(9)  # 选择9人棋盘
        board.placements["g1"][0] = "open"  # 访问 'g1' 键
        board.placements["g1"][0] = "open"
        self.assertFalse(board.move_piece("g1", "g4"))

    def test_occupied_to_pos(self):
        board.placements["g4"][0] = "white"
        self.assertFalse(board.move_piece("g1", "g4"))
        board.placements["g4"][0] = "open"

    def test_valid_move(self):

        board.placements["g1"][0] = "white"
        board.placements["g4"][6] = tk.Button()
        board.placements["g1"][6] = tk.Button()
        self.assertEqual(board.placements["g4"][0], "open")
        self.assertTrue(board.move_piece("g1", "g4"))
        board.placements["g4"][0] = "open"
        board.placements["g4"][6] = None
        board.placements["g1"][6] = None


class TestSettingUpGame(unittest.TestCase):
    '''
    def setUp(self):
        self.board = Board(SetUp)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
        }
        self.board.setUp()
    '''
    def test_initial_setup(self):
        board = Board(setup)
        self.assertEqual(board.gameType, 9)
        self.assertTrue(all(pos[0] == "open" for pos in board.placements.values()))
        self.assertEqual(white.getBankPieces(), 9)
        self.assertEqual(black.getBankPieces(), 9)


class TestPlacingAPiece(unittest.TestCase):
    '''
    def setUp(self):
        self.board = Board(SetUp)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
        }
        self.board.setUp()
        self.board.current_turn = "white"
    '''
    def test_place_piece(self):
        board.onButtonPress(board.placements["a1"], canvas, turn, origin="")
        self.assertEqual(board.placements["a1"][0], "white")
        self.assertEqual(white.getBankPieces(), 8)
        self.assertEqual(turn.getTurn(), "black")


class TestFlyingAPiece(unittest.TestCase):
    '''
    def setUp(self):
        # 初始化棋盘
        self.board = Board(setUp=Board)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["white", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
        }
        white.setPieces(3)
        self.turn = Turn("white")  # 创建一个 Turn 对象
    '''
    def test_fly_piece(self):
        # 白方飞棋
        board.onButtonPress(board.placements["a1"], canvas, turn, origin="a1")
        board.onButtonPress(board.placements["a4"], canvas, turn, origin="a1")
        self.assertEqual(board.placements["a1"][0], "open")
        self.assertEqual(board.placements["a4"][0], "white")



class TestRemovingAnOpponentsPiece(unittest.TestCase):
    '''
    def setUp(self):
        # 创建 Board 实例并设置初始状态
        self.board = Board()
        self.board.setUpBoard(9)  # 设定为9人棋盘
        self.board.placements = {
            "a1": ["white", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["white", "noMill", 20, 245, "a4", ["a1", "a7"], None],
            "a7": ["white", "noMill", 20, 480, "a7", ["a4", "d7"], None],
            "b2": ["black", "noMill", 105, 90, "b2", ["a1", "c2"], None],
        }
    '''
    def test_remove_opponent_piece(self):
        # 设置某个位置为黑色
        board.placements["b2"][0] = "black"

        # 调用移除棋子的操作
        board.removeOpponentPiece("black")

        # 断言 'b2' 位置应该是 "open"
        self.assertEqual(board.placements["b2"][0], "open")


class TestDeterminingIfGameIsOver(unittest.TestCase):
    def setUp(self):
        self.board = Board(SetUp)
        self.game_over = GameOver()
        black.setPieces(2)
        white.setPieces(5)

    def test_game_over(self):
        is_game_over = self.game_over.gameOver(black.getPlayerPieces(), white.getPlayerPieces())
        self.assertTrue(is_game_over)
        self.assertEqual(self.game_over.winner, "white")


if __name__ == '__main__':
    unittest.main()
