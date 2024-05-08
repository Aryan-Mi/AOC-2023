# Day 3: Gear Ratios https://adventofcode.com/2023/day/3


def main():
    # lines = open("Day-03/test.txt").read().splitlines()
    lines = open("Day-03/input.txt").read().splitlines()
    lines = [[*line] for line in lines]

    # Part 1
    solution1 = part1(lines)
    print("Part 1 solution:", solution1)

    # Part 2
    solution2 = part2(lines)
    print("Part 2 solution:", solution2)


neighbors_indices = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


# Sum all number parts
def part1(lines: list[list[str]]) -> int:
    sum = 0
    for i in range(len(lines)):
        isPartNumber = False
        partNumber = ""
        for j, char in enumerate(lines[i]):
            if char.isdigit():
                partNumber += char
                if isPartNumber:
                    continue
                for di, dj in neighbors_indices:
                    x, y = i + di, j + dj
                    if 0 <= x < len(lines) and 0 <= y < len(lines[i]):
                        if isSymbol(lines[x][y]):
                            isPartNumber = True
                            break
            else:
                if isPartNumber:
                    sum += int(partNumber)
                    isPartNumber = False
                partNumber = ""
                continue
        else:  # Reached the end of the line
            if isPartNumber:
                sum += int(partNumber)
    return sum


def part2(lines: list[list[str]]) -> int:
    sum = 0
    for i in range(len(lines)):
        for j, char in enumerate(lines[i]):
            if char == "*":
                neighbor_coords: list[list[int]] = []
                for di, dj in neighbors_indices:
                    x, y = i + di, j + dj
                    if 0 <= x < len(lines) and 0 <= y < len(lines[i]):
                        if lines[x][y].isdigit():
                            if len(neighbor_coords) > 0:
                                if (
                                    neighbor_coords[-1][0] == x
                                    and neighbor_coords[-1][1] == y - 1
                                ):
                                    neighbor_coords[-1][1] = y
                                else:
                                    neighbor_coords.append([x, y])
                            else:
                                neighbor_coords.append([x, y])
                if len(neighbor_coords) == 2:
                    gear_1 = getGearValue(lines, neighbor_coords[0])
                    gear_2 = getGearValue(lines, neighbor_coords[1])
                    sum += int(gear_1) * int(gear_2)
                neighbor_coords = []
    return sum


# Auxiliary functions
def isSymbol(char: str):
    return char != "." and not char.isalnum()


def getGearValue(lines: list[list[str]], coords: list[int]):
    [x, y] = coords
    [i, j] = [y - 1, y + 1]

    value = lines[coords[0]][coords[1]]
    prefix = ""
    while i >= 0:
        if lines[x][i].isdigit():
            prefix = lines[coords[0]][i] + prefix
        else:
            break
        i -= 1

    suffix = ""
    while j < len(lines[x]):
        if lines[x][j].isdigit():
            suffix += lines[coords[0]][j]
        else:
            break
        j += 1
    return prefix + value + suffix


# Execute the main function
if __name__ == "__main__":
    main()
