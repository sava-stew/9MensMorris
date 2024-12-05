import tkinter as tk
import unittest
from Board import Board, black, white
from GameOver import GameOver
from SetUp import SetUp
from Turn import Turn



class TestMovePiece(unittest.TestCase):

    def setUp(self):
        # 初始化 SetUp 实例（假设它是一个类）
        self.setUpInstance = SetUp()  # 替换为您的 SetUp 实例化逻辑
        self.board = Board(self.setUpInstance)  # 创建 Board 实例并传入 setUpInstance

    def test_invalid_from_pos(self):
        self.assertNotIn("g2", self.placements)
        self.assertFalse(self.board.move_piece("g2", "g4"))

    def test_invalid_to_pos(self):
        self.assertNotIn("g3", self.placements)
        self.assertFalse(self.board.move_piece("g1", "g3"))

    def test_empty_from_pos(self):
        self.setUpBoard(9)  # 选择9人棋盘
        self.placements["g1"][0] = "open"  # 访问 'g1' 键
        self.placements["g1"][0] = "open"
        self.assertFalse(self.board.move_piece("g1", "g4"))

    def test_occupied_to_pos(self):
        self.placements["g4"][0] = "white"
        self.assertFalse(self.board.move_piece("g1", "g4"))
        self.placements["g4"][0] = "open"

    def test_valid_move(self):

        self.placements["g1"][0] = "white"
        self.placements["g4"][6] = tk.Button()
        self.placements["g1"][6] = tk.Button()
        self.assertEqual(self.placements["g4"][0], "open")
        self.assertTrue(self.board.move_piece("g1", "g4"))
        self.placements["g1"][0] = "open"
        self.placements["g4"][6] = None
        self.placements["g1"][6] = None


class TestSettingUpGame(unittest.TestCase):
    def setUp(self):
        self.board = Board(SetUp)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
        }
        self.board.setUp()

    def test_initial_setup(self):
        self.assertEqual(self.board.gameType, 9)
        self.assertTrue(all(pos[0] == "open" for pos in self.board.placements.values()))
        self.assertEqual(white.getBankPieces(), 9)
        self.assertEqual(black.getBankPieces(), 9)


class TestPlacingAPiece(unittest.TestCase):
    def setUp(self):
        self.board = Board(SetUp)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
        }
        self.board.setUp()
        self.board.current_turn = "white"

    def test_place_piece(self):
        self.board.onButtonPress(self.board.placements["a1"], None, self.board.current_turn, origin="")
        self.assertEqual(self.board.placements["a1"][0], "white")
        self.assertEqual(white.getBankPieces(), 8)
        self.assertEqual(self.board.current_turn, "black")


class TestFlyingAPiece(unittest.TestCase):
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

    def test_fly_piece(self):
        # 白方飞棋
        self.board.onButtonPress(self.board.placements["a1"], None, self.turn, origin="a1")
        self.board.onButtonPress(self.board.placements["a4"], None, self.turn, origin="a1")
        self.assertEqual(self.board.placements["a1"][0], "open")
        self.assertEqual(self.board.placements["a4"][0], "white")



class TestRemovingAnOpponentsPiece(unittest.TestCase):
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

    def test_remove_opponent_piece(self):
        # 设置某个位置为黑色
        self.board.placements["b2"][0] = "black"

        # 调用移除棋子的操作
        self.board.removeOpponentPiece("black")

        # 断言 'b2' 位置应该是 "open"
        self.assertEqual(self.board.placements["b2"][0], "open")


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
