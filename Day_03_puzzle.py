def get_input():
    input = 'Day_03_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        return raw_input

def find_parts(engine_map):
    map_width = len(engine_map[0])
    map_height = len(engine_map)
    part_nums = []
    gear_ratios = []
    for row in range(map_height):
        for col in range(map_width):
            part_num = ''
            gear_ratio = []
            if engine_map[row][col] != '.' and not engine_map[row][col].isnumeric():
                if col < map_width - 1:
                    if engine_map[row][col + 1].isnumeric():
                        part_num += engine_map[row][col + 1]
                        if col + 1 < map_width - 1:
                            if engine_map[row][col + 2].isnumeric():
                                part_num += engine_map[row][col + 2]
                                if col + 2 < map_width - 1:
                                    if engine_map[row][col + 3].isnumeric():
                                        part_num += engine_map[row][col + 3]
                        part_nums.append(int(part_num))
                        if engine_map[row][col] == '*':
                            gear_ratio.append(int(part_num))
                        part_num = ''
                if col > 0:
                    if engine_map[row][col - 1].isnumeric():
                        part_num += engine_map[row][col - 1]
                        if col - 1 > 0:
                            if engine_map[row][col - 2].isnumeric():
                                part_num = engine_map[row][col - 2] + part_num
                                if col - 2 > 0:
                                    if engine_map[row][col - 3].isnumeric():
                                        part_num = engine_map[row][col - 3] + part_num
                        part_nums.append(int(part_num))
                        if engine_map[row][col] == '*':
                            gear_ratio.append(int(part_num))
                        part_num = ''
                if row > 0:
                    if engine_map[row - 1][col].isnumeric():
                        part_num += engine_map[row - 1][col]
                        if col > 0:
                            if engine_map[row - 1][col - 1].isnumeric():
                                part_num = engine_map[row - 1][col - 1] + part_num
                                if col - 1 > 0:
                                    if engine_map[row - 1][col - 2].isnumeric():
                                        part_num = engine_map[row - 1][col - 2] + part_num
                        if col < map_width - 1:
                            if engine_map[row - 1][col + 1].isnumeric():
                                part_num += engine_map[row - 1][col + 1]
                                if col + 1 < map_width - 1:
                                    if engine_map[row - 1][col + 2].isnumeric():
                                        part_num += engine_map[row - 1][col + 2]
                        part_nums.append(int(part_num))
                        if engine_map[row][col] == '*':
                            gear_ratio.append(int(part_num))
                        part_num = ''
                    else:
                        if col > 0:
                            if engine_map[row - 1][col -1].isnumeric():
                                part_num += engine_map[row - 1][col - 1]
                                if col - 1 > 0:
                                    if engine_map[row - 1][col - 2].isnumeric():
                                        part_num = engine_map[row - 1][col - 2] + part_num
                                        if col - 2 > 0:
                                            if engine_map[row - 1][col - 3].isnumeric():
                                                part_num = engine_map[row - 1][col - 3] + part_num
                                part_nums.append(int(part_num))
                                if engine_map[row][col] == '*':
                                    gear_ratio.append(int(part_num))
                                part_num = ''
                        if col < map_width - 1:
                            if engine_map[row - 1][col + 1].isnumeric():
                                part_num += engine_map[row - 1][col + 1]
                                if col + 1 < map_width - 1:
                                    if engine_map[row - 1][col + 2].isnumeric():
                                        part_num += engine_map[row - 1][col + 2]
                                        if col + 2 < map_width - 1:
                                            if engine_map[row - 1][col + 3].isnumeric():
                                                part_num += engine_map[row - 1][col + 3]
                                part_nums.append(int(part_num))
                                if engine_map[row][col] == '*':
                                    gear_ratio.append(int(part_num))
                                part_num = ''
                if row < map_height - 1:
                    if engine_map[row + 1][col].isnumeric():
                        part_num += engine_map[row + 1][col]
                        if col > 0:
                            if engine_map[row + 1][col - 1].isnumeric():
                                part_num = engine_map[row + 1][col - 1] + part_num
                                if col - 1 > 0:
                                    if engine_map[row + 1][col - 2].isnumeric():
                                        part_num = engine_map[row + 1][col - 2] + part_num
                        if col < map_width - 1:
                            if engine_map[row + 1][col + 1].isnumeric():
                                part_num += engine_map[row + 1][col + 1]
                                if col + 1 < map_width - 1:
                                    if engine_map[row + 1][col + 2].isnumeric():
                                        part_num += engine_map[row + 1][col + 2]
                        part_nums.append(int(part_num))
                        if engine_map[row][col] == '*':
                            gear_ratio.append(int(part_num))
                        part_num = ''
                    else:
                        if col > 0:
                            if engine_map[row + 1][col -1].isnumeric():
                                part_num += engine_map[row + 1][col - 1]
                                if col - 1 > 0:
                                    if engine_map[row + 1][col - 2].isnumeric():
                                        part_num = engine_map[row + 1][col - 2] + part_num
                                        if col - 2 > 0:
                                            if engine_map[row + 1][col - 3].isnumeric():
                                                part_num = engine_map[row + 1][col - 3] + part_num
                                part_nums.append(int(part_num))
                                if engine_map[row][col] == '*':
                                    gear_ratio.append(int(part_num))
                                part_num = ''
                        if col < map_width - 1:
                            if engine_map[row + 1][col + 1].isnumeric():
                                part_num += engine_map[row + 1][col + 1]
                                if col + 1 < map_width - 1:
                                    if engine_map[row + 1][col + 2].isnumeric():
                                        part_num += engine_map[row + 1][col + 2]
                                        if col + 2 < map_width - 1:
                                            if engine_map[row + 1][col + 3].isnumeric():
                                                part_num += engine_map[row + 1][col + 3]
                                part_nums.append(int(part_num))
                                if engine_map[row][col] == '*':
                                    gear_ratio.append(int(part_num))
                                part_num = ''
            if len(gear_ratio) == 2:
                gear_ratios.append(gear_ratio[0] * gear_ratio[1])
    part1 = 0
    for part in part_nums:
        part1 += part
    print(part1)
    part2 = 0
    for ratio in gear_ratios:
        part2 += ratio
    print(part2)

def main():
    engine_map = get_input()
    find_parts(engine_map)

if __name__ == '__main__':
    main()