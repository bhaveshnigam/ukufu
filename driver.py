#! /usr/bin/python
import argparse
from rover import Rover, LandGrid

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lets explore the plateau')
    parser.add_argument('--file', dest='filename', required=True,
                        help='File to read the data from.')
    args = parser.parse_args()

    with open(args.filename, 'r') as data_file:
        all_lines = data_file.readlines()
        land_grid_dimensions = all_lines[0].split()
        land = LandGrid(int(land_grid_dimensions[0]), int(land_grid_dimensions[1]))
        for rover_conf in all_lines[1:]:
            conf = rover_conf.split()
            rover = Rover(land)
            rover.explore(int(conf[0]), int(conf[1]), conf[2], conf[3])
            print(rover.get_rover_position())
