def get_input():
    input = 'Day_12_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        spr_strs = []
        spr_key_strs = []
        for line in raw_input:
            str_key_pair = line.split(' ')
            spr_strs.append(str_key_pair[0])
            spr_key_strs.append(str_key_pair[1])
        spr_keys = []
        for str in spr_key_strs:
            key_num_strs = str.split(',')
            key_nums = [int(num) for num in key_num_strs]
            spr_keys.append(key_nums)
        return spr_strs, spr_keys

def repair_checker(spr_str, spr_key):
    spr_key = tuple(spr_key)
    active_strs = {}
    for spr in spr_str:
        new_strs = {}
        if active_strs == {}:
            if spr == '.':
                active_strs[(0,)] = 1
            elif spr == '#':
                active_strs[(1,)] = 1
            else:
                active_strs[(0,)] = 1
                active_strs[(1,)] = 1
        elif spr == '.':
            for active_str in active_strs:
                if active_str[-1] != 0:
                    if active_str + (0,) in active_strs:
                        active_strs[active_str + (0,)] = active_strs[active_str] + active_strs[active_str + (0,)]
                    else:
                        new_strs[active_str + (0,)] = active_strs[active_str]
            for active_str in active_strs:
                if active_str[-1] == 0:
                    new_strs[active_str] = active_strs[active_str]
            active_strs = new_strs
        elif spr == '#':
            for active_str in active_strs:
                new_strs[active_str[:-1] + (active_str[-1] + 1,)] = active_strs[active_str]
            active_strs = new_strs
        else:
            for active_str in active_strs:
                new_strs[active_str[:-1] + (active_str[-1] + 1,)] = active_strs[active_str]
            for active_str in active_strs:
                if active_str[-1] != 0:
                    if active_str + (0,) in active_strs:
                        active_strs[active_str + (0,)] = active_strs[active_str] + active_strs[active_str + (0,)]
                    else:
                        new_strs[active_str + (0,)] = active_strs[active_str]
            for active_str in active_strs:
                if active_str[-1] == 0:
                    new_strs[active_str] = active_strs[active_str]
            active_strs = new_strs
        dead_strs = []
        for active_str in active_strs:
            if len(active_str) > (len(spr_key) + 1):
                dead_strs.append(active_str)
            else:
                for index in range(len(active_str) - 1):
                    if active_str[index] != spr_key[index]:
                        dead_strs.append(active_str)
        for str in dead_strs:
            active_strs.pop(str)
    valid_strs = 0
    if spr_key in active_strs:
        valid_strs += active_strs[spr_key]
    if (spr_key + (0,)) in active_strs:
        valid_strs += active_strs[spr_key + (0,)]
    return valid_strs

def main():
    spr_strs, spr_keys = get_input()
    part1 = 0
    for index in range(len(spr_strs)):
        part1 += repair_checker(spr_strs[index], spr_keys[index])
    print(part1)
    spr_strs = [spr_str + '?' + spr_str + '?' + spr_str + '?' + spr_str + '?' + spr_str for spr_str in spr_strs]
    spr_keys = [spr_key + spr_key + spr_key + spr_key + spr_key for spr_key in spr_keys]
    part2 = 0
    for index in range(len(spr_strs)):
        part2 += repair_checker(spr_strs[index], spr_keys[index])
    print(part2)

if __name__ == '__main__':
    main()