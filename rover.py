class LandGrid(object):
    """The land grid is a first quadrant based grid instead of regular fourth quadrant grid."""

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.grid = []
        for i in range(max_x + 1):
            row = []
            for j in range(max_y + 1):
                row.append(0)
            self.grid.append(row)

    def _convert_coordinates(self, x, y):
        """Converts fourth quadrant co-ordinates to first quadrant co-ordinates."""
        return self.max_y - y, x


    def print_grid(self):
        for x in self.grid:
            print(x)

    def empty_coordinate(self, x, y):
        """Empties the provided co-ordinate."""
        converted_x, converted_y = self._convert_coordinates(x, y)
        self.grid[converted_x][converted_y] = 0
        return x, y

    def place_item(self, x, y):
        """Marks the provided co-ordinate as occupied."""
        converted_x, converted_y = self._convert_coordinates(x, y)
        self.grid[converted_x][converted_y] = 1
        return x, y


class Rover(object):

    DIRECTIONS = ['N', 'E', 'W', 'S']
    ORIENTATIONS = [90, 0, 180, 270]

    DIRECTION_TO_ORIENTATION = dict(zip(DIRECTIONS, ORIENTATIONS))
    ORIENTATION_TO_DIRECTION = dict(zip(ORIENTATIONS, DIRECTIONS))

    def __init__(self, landscape):
        self.orientation = 90
        self.position_x = 0
        self.position_y = 0
        self.landscape = landscape

    def move(self):
        """Move the rover in the oriented direction, one step at a time."""
        if self.orientation == 90:
            self.landscape.empty_coordinate(self.position_x, self.position_y)
            self.position_x, self.position_y = self.landscape.place_item(self.position_x, self.position_y + 1)
        elif self.orientation == 0:
            self.landscape.empty_coordinate(self.position_x, self.position_y)
            self.position_x, self.position_y = self.landscape.place_item(self.position_x + 1, self.position_y)
        elif self.orientation == 180:
            self.landscape.empty_coordinate(self.position_x, self.position_y)
            self.position_x, self.position_y = self.landscape.place_item(self.position_x - 1, self.position_y)
        elif self.orientation == 270:
            self.landscape.empty_coordinate(self.position_x, self.position_y)
            self.position_x, self.position_y = self.landscape.place_item(self.position_x, self.position_y - 1)

    def _fix_orientation(self):
        if self.orientation == -90:
            self.orientation = 270
        elif self.orientation == -270:
            self.orientation = 90
        elif self.orientation == -180:
            self.orientation = 180
        elif self.orientation == -270:
            self.orientation = 90
        elif self.orientation == 360:
            self.orientation = 0

    def explore(self, current_x, current_y, current_orientation, explore_command_sequence):
        self.position_x = current_x
        self.position_y = current_y
        self.landscape.place_item(self.position_x, self.position_y)
        self.orientation = self.DIRECTION_TO_ORIENTATION.get(current_orientation)

        for command in explore_command_sequence:
            self._fix_orientation()

            if command == 'L':
                self.orientation += 90
            elif command == 'R':
                self.orientation -= 90
            elif command == 'M':
                self.move()

        self._fix_orientation()

    def get_rover_position(self):
        return '%s %s %s' % (self.position_x, self.position_y, self.ORIENTATION_TO_DIRECTION.get(self.orientation))
