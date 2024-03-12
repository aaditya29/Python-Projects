"""
Assumptions:

- data directory contains many files and directories
- we are only interested in the games contained in this directory
- each game is stored in a directory that contains the word "game"
- each game directory contains a single .go file that must be compiled before it can be run


Project Steps/Requirements:

- Find all game directories from /data
- Create a new /games directory 
- Copy and remove the "game" suffix of all games into the /games directory
- Create a .json file with the information about the games
- Compile all of the game code 
- Run all of the game code-
"""
import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"


def find_all_game_paths(source):  # to fetch game path
    game_paths = []
    # walk will recursively throw directly we passed in os command i.e. look all the files inside directory
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break
    return game_paths


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main(source, target):
    cwd = os.getcwd()  # getting current working directory
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    print(game_paths)


# grabbing command line arguments
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass only source and target directory.")

    # stripping name of our python files which we don't want
    source, target = args[1:]
    main(source, target)
