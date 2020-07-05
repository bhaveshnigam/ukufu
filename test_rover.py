import unittest
from rover import Rover, LandGrid


class RoverTestCases(unittest.TestCase):
    """Test cases to test Rover and LandGrid classes"""

    def test_land_grid_creation(self):
        land = LandGrid(2, 2)
        expected_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(land.grid, expected_grid)

    def test_land_grid_for_placing_item(self):
        land = LandGrid(2, 2)
        expected_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
        ]
        land.place_item(0, 0)
        self.assertEqual(land.grid, expected_grid)

        expected_grid = [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0],
        ]
        land.place_item(2, 2)
        self.assertEqual(land.grid, expected_grid)

        expected_grid = [
            [0, 0, 1],
            [0, 0, 1],
            [1, 0, 0],
        ]
        land.place_item(2, 1)
        self.assertEqual(land.grid, expected_grid)

    def test_land_grid_for_clearing_item(self):
        land = LandGrid(2, 2)
        land.place_item(0, 0)
        land.place_item(2, 2)
        land.place_item(2, 1)
        expected_grid = [
            [0, 0, 1],
            [0, 0, 1],
            [1, 0, 0],
        ]
        self.assertEqual(land.grid, expected_grid)
        land.empty_coordinate(2, 1)
        expected_grid = [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0],
        ]
        self.assertEqual(land.grid, expected_grid)

    def test_rover_explore(self):
        land = LandGrid(5, 5)
        rover = Rover(land)
        expected_position = '1 3 N'
        rover.explore(1, 2, 'N', 'LMLMLMLMM')
        ending_position = rover.get_rover_position()
        self.assertEqual(ending_position, expected_position)

    def test_rover_explore_with_no_explore(self):
        land = LandGrid(5, 5)
        rover = Rover(land)
        expected_position = '1 2 N'
        rover.explore(1, 2, 'N', '')
        ending_position = rover.get_rover_position()
        self.assertEqual(ending_position, expected_position)

    def test_rover_explore_with_only_right(self):
        land = LandGrid(5, 5)
        rover = Rover(land)
        expected_position = '1 2 S'
        rover.explore(1, 2, 'N', 'RR')
        ending_position = rover.get_rover_position()
        self.assertEqual(ending_position, expected_position)

    def test_rover_explore_with_only_left(self):
        land = LandGrid(5, 5)
        rover = Rover(land)
        expected_position = '1 2 S'
        rover.explore(1, 2, 'N', 'LL')
        ending_position = rover.get_rover_position()
        self.assertEqual(ending_position, expected_position)

    def test_rover_explore_with_only_move(self):
        land = LandGrid(5, 5)
        rover = Rover(land)
        expected_position = '1 4 N'
        rover.explore(1, 2, 'N', 'MM')
        ending_position = rover.get_rover_position()
        self.assertEqual(ending_position, expected_position)


if __name__ == '__main__':
    unittest.main()
