
import tkinter as tk

import unittest
from Board import Board, black, white, game
from Turn import Turn
from Player import Player
from GameOver import GameOver
from SetUp import SetUp

board = Board(SetUp)
placements = board.placements

class TestMovePiece(unittest.TestCase):
    def test_invalid_from_pos(self):
        self.assertNotIn("g2", self.board.placements)
        self.assertFalse(Board.move_piece(self, "g2", "g4"))
    def test_invalid_to_pos(self):
        self.assertNotIn("g3", self.board.placements)
        self.assertFalse(Board.move_piece(self, "g1", "g3"))
    def test_empty_from_pos(self):
        self.assertEqual(self.board.placements["g1"][0],"open")
        self.assertFalse(Board.move_piece(self, "g1", "g4"))
    def test_occupied_to_pos(self):
        placements["g4"][0] = "white"
        self.assertFalse(Board.move_piece(self, "g1", "g4"))
        self.board.placements["g4"][0] = "open"
    def test_valid_move(self):
        placements["g1"][0] = "white"
        placements["g4"][6] = tk.Button()
        placements["g1"][6] = tk.Button()
        self.assertEqual(placements["g4"][0],"open")
        self.assertTrue(Board.move_piece(self, "g1", "g4"))
        placements["g1"][0] = "open"
        placements["g4"][6] = None
        placements["g1"][6] = None

class TestSettingUpGame(unittest.TestCase):
    def setUp(self):
            # 初始化一个 9 男棋游戏
        self.board = Board(setUp=Board)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
            }
        self.board.setUp()

    def test_initial_setup(self):
            # 检查游戏类型
        self.assertEqual(self.board.gameType, 9)
            # 检查所有位置是否初始化为 open
        self.assertTrue(all(pos[0] == "open" for pos in self.board.placements.values()))
            # 检查玩家初始棋子数量
        self.assertEqual(white.getBankPieces(), 9)
        self.assertEqual(black.getBankPieces(), 9)

class TestPlacingAPiece(unittest.TestCase):
    def setUp(self):
            # 初始化棋盘
        self.board = Board(setUp=Board)
        self.board.gameType = 9
        self.board.placements = {
            "a1": ["open", "noMill", 20, 20, "a1", ["a4", "d1"], None],
            "a4": ["open", "noMill", 20, 245, "a4", ["a1", "a7"], None],
            }
        self.board.setUp()
        self.board.current_turn = "white"

    def test_place_piece(self):
            # 白方放置棋子到 a1
        self.board.onButtonPress(self.board.placements["a1"], None, self.board.current_turn, origin="")
        self.assertEqual(self.board.placements["a1"][0], "white")
        self.assertEqual(white.getBankPieces(), 8)  # 白方银行棋子数减少
        self.assertEqual(self.board.current_turn, "black")  # 轮到黑方

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

    def test_fly_piece(self):
            # 白方飞棋
        self.board.onButtonPress(self.board.placements["a1"], None, "white", origin="a1")
        self.board.onButtonPress(self.board.placements["a4"], None, "white", origin="a1")
        self.assertEqual(self.board.placements["a1"][0], "open")
        self.assertEqual(self.board.placements["a4"][0], "white")

class TestRemovingAnOpponentsPiece(unittest.TestCase):
    def setUp(self):
            # 初始化棋盘
        self.board = Board(setUp=Board)
        self.board.gameType = 9
        self.board.placements = {
                "a1": ["white", "noMill", 20, 20, "a1", ["a4", "d1"], None],
                "a4": ["white", "noMill", 20, 245, "a4", ["a1", "a7"], None],
                "a7": ["white", "noMill", 20, 480, "a7", ["a4", "d7"], None],
                "b2": ["black", "noMill", 105, 90, "b2", ["a1", "c2"], None],
            }
        self.board.setUp()

    def test_remove_opponent_piece(self):
            # 检查形成白方的 Mill 并移除黑方的棋子
        self.board.checkMills()
        self.assertEqual(self.board.placements["b2"][0], "open")
        self.assertEqual(black.getPlayerPieces(), 8)

class TestDeterminingIfGameIsOver(unittest.TestCase):
    def setUp(self):
            # 初始化棋盘
        self.board = Board(setUp=Board)
        self.board.gameType = 9
        black.setPieces(2)
        white.setPieces(5)

    def test_game_over(self):
            # 检查游戏是否结束
        game_over = game.gameOver(black.getPlayerPieces(), white.getPlayerPieces())
        self.assertTrue(game_over)
        self.assertEqual(game.winner, "white")  # 假设白方获胜


if __name__ == '__main__':
    unittest.main()
