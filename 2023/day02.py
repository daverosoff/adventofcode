import numpy as np

with open('input02.dat', 'r') as f:
    puzzle = f.read()

sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def parse_line(puzzle_line: str) -> dict:
    if puzzle_line:
        id_string, cubes_string = puzzle_line.split(": ")
        id_string = id_string.split()[-1]
        cubes_list = cubes_string.split('; ')
        rgb_lists = []
        for cl in cubes_list:
            rgb_list = [0, 0, 0]
            for cn in cl.split(", "):
                cubes, color = cn.split()
                match color:
                    case "red": rgb_list[0] += int(cubes)
                    case "green": rgb_list[1] += int(cubes)
                    case "blue": rgb_list[2] += int(cubes)
            rgb_lists.append(np.asarray(rgb_list))
        return {int(id_string): rgb_lists}
    else:
        return {}

def puzz01(puzz: str) -> int:
    games_dict = {}
    result = 0
    for line in puzz.split('\n'):
        if line:
            games_dict.update(parse_line(line))
    for id, rgb_lists in games_dict.items():
        if all(
            [
                (rgb_list <= np.asarray([12, 13, 14])).all()
                for rgb_list in rgb_lists
            ]
         ):
            result += id
    return result

def puzz02(puzz: str) -> int :
    games_dict = {}
    result = 0
    for line in puzz.split('\n'):
        if line:
            games_dict.update(parse_line(line))
    for id, rgb_lists in games_dict.items():
        alists = np.asarray(rgb_lists)
        maxs = np.max(alists, 0)
        result += maxs[0] * maxs[1] * maxs[2]
    return result

print(puzz01(sample))
print(puzz01(puzzle))
print(puzz02(sample))
print(puzz02(puzzle))