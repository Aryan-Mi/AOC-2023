# Day 2: Cube Conundrum
import numpy as np


def main():
    lines = open("Day-02/input.txt").read().splitlines()

    # Part 1
    valid_games = [game_id for game in lines if (game_id := validate_game(game)) != 0]
    print("Part 1 \ntotal sum:", sum(valid_games))
    # Part 2
    game_powers = sum([game_powerset(game) for game in lines])
    print("Part 2 \ntotal power sum:", game_powers)


# Part 1
def validate_game(game: str) -> int:
    cube_dict = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    array = game.split(":")
    (id, subsets) = (array[0][5:], array[1].strip().split("; "))

    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            [count, color] = cube.split(" ")
            if cube_dict[color] < int(count):
                return 0
    return int(id)


# Part 2
def game_powerset(game: str) -> int:
    cube_dict = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    array = game.split(":")
    subsets = array[1].strip().split("; ")

    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            [count, color] = cube.split(" ")
            if cube_dict[color] < int(count):
                cube_dict[color] = int(count)
    return np.prod(list(cube_dict.values()))


main()
