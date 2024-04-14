import unittest
from ticTacToeBored import check_winner

class TestGame(unittest.TestCase):
    def test_check_row(self):
        # Test case: Check row
        board = [[1,1,1],[0,0,0],[0,0,0]]
        result = check_winner(board)  # Add your arguments here
        self.assertEqual(result[0], 1, "Checking row - Expected player 1 to be the winner")
        self.assertEqual(result[1], True, "Checking row - Expected game_over to be set to True")

    def test_check_column(self):
            # Test case: Check columns
        board = [[1,0,0],[1,0,0],[1,0,0]]
        result = check_winner(board)  # Add your arguments here
        self.assertEqual(result[0], 1, "Checking column - Expected player 1 to be the winner")
        self.assertEqual(result[1], True, "Checking column - Expected game_over to be set to True")

    def test_check_diagonals(self):
        # Test case: Check diagonals Upper left to lower right
        board = [[1,0,0],[0,1,0],[0,0,1]]
        result = check_winner(board)  # Add your arguments here
        self.assertEqual(result[0], 1, "Checking diagonal 1 - Expected player 1 to be the winner")
        self.assertEqual(result[1], True, "Checking diagonal 1 - Expected game_over to be set to True")
    
        # Test case: Check diagonals: Lower left to upper right
        board = [[0,0,1],[0,1,0],[1,0,0]]
        result = check_winner(board)  # Add your arguments here
        self.assertEqual(result[0], 1, "Checking diagonal 2 - Expected player 1 to be the winner")
        self.assertEqual(result[1], True, "Checking diagonal 2 - Expected game_over to be set to True")

    def test_check_tie(self):
        # Test case: Check for tie
        board = [[1,-1,-1],[-1,1,1],[1,-1,-1]]
        result = check_winner(board)  # Add your arguments here
        self.assertEqual(result[0], 0, "Checking tie - Expected player 0 to be the winner")
        self.assertEqual(result[1], True, "Checking tie - Expected game_over to be set to True")
    

if __name__ == '__main__':
    unittest.main()