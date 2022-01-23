import unittest
import Settings
from Player import Player


class PlayerTests(unittest.TestCase):
    """
    Player test cases.
    """

    p = Player()

    def test_player_getters(self):
        """ tests correctness of getter methods """
        self.assertEqual(self.p.get_x(), Settings.PLAYER_INITIAL_COORDINATES[0])
        self.assertEqual(self.p.get_y(), Settings.PLAYER_INITIAL_COORDINATES[1])
        self.assertEqual(self.p.get_speed(), Settings.PLAYER_BLOCK_DOWN_SPEED)

    def test_move_left(self):
        """ tests leftward movement """
        old_x = self.p.get_x()
        self.p.move_left()
        self.assertEqual(self.p.get_x(), old_x - self.p.get_speed())

    def test_move_right(self):
        """ test rightward movement """
        old_x = self.p.get_x()
        self.p.move_right()
        self.assertEqual(self.p.get_x(), old_x + self.p.get_speed())

    def test_block(self):
        """ tests defensive mode """
        self.p.block_up()
        self.assertEqual(self.p.get_speed(), Settings.PLAYER_BLOCK_UP_SPEED)
        self.p.block_down()
        self.assertEqual(self.p.get_speed(), Settings.PLAYER_BLOCK_DOWN_SPEED)


if __name__ == '__main__':
    unittest.main()
