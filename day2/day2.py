games = {}
with open("input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        if line:
            line = line.split(":")
            game_id = int(line[0].split(" ")[1])
            cube_sets = line[1].strip().split(";")
            games[game_id] = []
            for cube_set in cube_sets:
                cubes = cube_set.split(",")
                cube_list = {}
                for cube in cubes:
                    cube = cube.strip()
                    count = int(cube.split(" ")[0])
                    color = cube.split(" ")[1]
                    cube_list[color] = count
                games[game_id].append(cube_list)

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

def valid_game(game):
    for draw in game:
        if "red" in draw:
            if draw["red"] > RED_CUBES: return False
        if "green" in draw:
            if draw["green"] > GREEN_CUBES: return False
        if "blue" in draw:
            if draw["blue"] > BLUE_CUBES: return False
    return True

sum = 0
for key, game in games.items():
    if valid_game(game):
        sum += key

print("Part 1 solution is", sum)

def set_power(game):
    red, green, blue = 0,0,0
    for draw in game:
        if "red" in draw:
            if draw["red"] > red: red = draw["red"]
        if "green" in draw:
            if draw["green"] > green: green = draw["green"]
        if "blue" in draw:
            if draw["blue"] > blue: blue = draw["blue"]
    return red*green*blue

power = 0
for key, game in games.items():
    power += set_power(game)

print("Part 2 solution is", power)