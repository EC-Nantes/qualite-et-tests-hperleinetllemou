import unittest
from game import TicTacToe, play
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TestTicTacToe(unittest.TestCase):
    def test_game_play(self):
        x_player = SmartComputerPlayer('X')
        o_player = HumanPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)

        # Assert that the game result is one of ['X', 'O', 'TIE']
        self.assertIn(result, ['X', 'O', 'TIE'])

    def test_minimax_algorithm(self):
        # Create a game state for testing minimax algorithm
        test_game = TicTacToe()
        test_game.board = ['X', 'O', 'X', ' ', ' ', ' ', 'O', ' ', 'O']

        smart_player = SmartComputerPlayer('X')
        result = smart_player.minimax(test_game, 'X')

        # Assert that the result has the expected structure
        self.assertIsInstance(result, dict)
        self.assertIn('position', result)
        self.assertIn('score', result)

if __name__ == '__main__':
    unittest.main()
