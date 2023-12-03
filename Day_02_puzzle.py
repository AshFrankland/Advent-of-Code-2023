def get_input():
    input = 'Day_02_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.lstrip('Game 1234567890').rstrip('\n'))
        game_dict = {}
        game_ID = 0
        for game in raw_input:
            game_ID += 1
            game_dict[game_ID] = {}
            draw = 0
            for char in range(len(game)):
                if game[char] == ':' or game[char] == ';':
                    draw += 1
                    game_dict[game_ID][draw] = {'r': 0, 'g': 0, 'b': 0}
                if game[char].isnumeric() and game[char + 1].isnumeric():
                    pass
                elif game[char].isnumeric() and game[char - 1].isnumeric():
                    game_dict[game_ID][draw][game[char + 2]] = int(game[char - 1] + game[char])
                elif game[char].isnumeric():
                    game_dict[game_ID][draw][game[char + 2]] = int(game[char])
        return game_dict

def check_games(game_dict):
    possible_games = []
    games_power = []
    for game in game_dict:
        red = 0
        green = 0
        blue = 0
        for draw in game_dict[game]:
            if game_dict[game][draw]['r'] > red:
                red = game_dict[game][draw]['r']
            if game_dict[game][draw]['g'] > green:
                green = game_dict[game][draw]['g']
            if game_dict[game][draw]['b'] > blue:
                blue = game_dict[game][draw]['b']
        if red <= 12 and green <= 13 and blue <= 14:
            possible_games.append(game)
        games_power.append(red * green * blue)
    part1 = 0
    for game in possible_games:
        part1 += game
    print(part1)
    part2 = 0
    for game in games_power:
        part2 += game
    print(part2)

def main():
    game_dict = get_input()
    check_games(game_dict)

if __name__ == '__main__':
    main()