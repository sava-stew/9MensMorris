import unittest
import tkinter as tk
from Board import Board
from Board import placements

class TestMovePiece(unittest.TestCase):
    def test_invalid_from_pos(self):
        self.assertNotIn("g2", placements)
        self.assertFalse(Board.move_piece(self, "g2", "g4"))
    def test_invalid_to_pos(self):
        self.assertNotIn("g3", placements)
        self.assertFalse(Board.move_piece(self, "g1", "g3"))
    def test_empty_from_pos(self):
        self.assertEqual(placements["g1"][0],"open")
        self.assertFalse(Board.move_piece(self, "g1", "g4"))
    def test_occupied_to_pos(self):
        placements["g4"][0] = "white"
        self.assertFalse(Board.move_piece(self, "g1", "g4"))
        placements["g4"][0] = "open"
    def test_valid_move(self):
        placements["g1"][0] = "white"
        placements["g4"][6] = tk.Button()
        placements["g1"][6] = tk.Button()
        self.assertEqual(placements["g4"][0],"open")
        self.assertTrue(Board.move_piece(self, "g1", "g4"))
        placements["g1"][0] = "open"
        placements["g4"][6] = None
        placements["g1"][6] = None

if __name__ == '__main__':
    unittest.main()
