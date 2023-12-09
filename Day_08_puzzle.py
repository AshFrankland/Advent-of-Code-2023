from math import lcm

def get_input():
    input = 'Day_08_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        dir_str = raw_input[0]
        raw_input.pop(0)
        raw_input.pop(0)
        map_dict = {}
        for line in raw_input:
            loc, dirs = line.split(' = ')
            dirs = dirs.lstrip('(').rstrip(')')
            L, R = dirs.split(', ')
            map_dict[loc] = {'L': L, 'R': R}
        return map_dict, dir_str

def follow_map(map_dict, dir_str):
    loc = 'AAA'
    index = 0
    steps = 0
    while loc != 'ZZZ':
        steps += 1
        loc = map_dict[loc][dir_str[index]]
        index += 1
        if index == len(dir_str):
            index = 0
    print(steps)

def ghost_maps(map_dict, dir_str):
    locs = []
    for loc in map_dict:
        if loc[-1] == 'A':
            locs.append(loc)
    steps = []
    for loc in locs:
        path = loc
        index = 0
        step = 0
        while path[-1] != 'Z':
            step += 1
            path = map_dict[path][dir_str[index]]
            index += 1
            if index == len(dir_str):
                index = 0
        steps.append(step)
    print(lcm(*steps))

def main():
    map_dict, dir_str = get_input()
    follow_map(map_dict, dir_str)
    ghost_maps(map_dict, dir_str)

if __name__ == '__main__':
    main()