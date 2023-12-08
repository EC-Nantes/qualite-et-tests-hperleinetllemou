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

    def test_empty_board(self):
        empty_game = TicTacToe()
        self.assertFalse(empty_game.game_over())
        self.assertEqual(empty_game.current_winner, None)

    def test_human_vs_random(self):
        human_player = HumanPlayer('X')
        random_player = RandomComputerPlayer('O')
        game = TicTacToe()

        while not game.game_over():
            # Human's turn
            game.make_move(human_player.get_move(game), human_player.letter)

            if game.game_over():
                break

            # Random Computer's turn
            game.make_move(random_player.get_move(game), random_player.letter)

        self.assertTrue(game.game_over())

    def test_smart_vs_random(self):
        smart_player = SmartComputerPlayer('X')
        random_player = RandomComputerPlayer('O')
        game = TicTacToe()

        while not game.game_over():
            # Smart Computer's turn
            game.make_move(smart_player.get_move(game), smart_player.letter)

            if game.game_over():
                break

            # Random Computer's turn
            game.make_move(random_player.get_move(game), random_player.letter)

        self.assertTrue(game.game_over())

if __name__ == '__main__':
    unittest.main()
