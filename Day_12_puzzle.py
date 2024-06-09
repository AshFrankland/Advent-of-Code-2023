from pprint import pprint

def get_input():
    #input = 'test_input.txt'
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
    active_strs = []
    checked_strs = []
    dots = []
    hashes = []
    for spr in spr_str:
        if spr == '.' and active_strs == []:
            pass
        elif spr == '#' and active_strs == []:
            active_strs = ['#']
        elif spr == '?' and active_strs == []:
            active_strs = ['.', '#']
        elif spr == '.':
            active_strs = [active_str + '.' for active_str in active_strs]
            for active_str in active_strs:
                if str_checker(active_str, spr_key):
                    checked_strs.append(active_str)
            active_strs = checked_strs
            checked_strs = []
        elif spr == '#':
            active_strs = [active_str + '#' for active_str in active_strs]
            for active_str in active_strs:
                if str_checker(active_str, spr_key):
                    checked_strs.append(active_str)
            active_strs = checked_strs
            checked_strs = []
        elif spr == '?':
            dots = [active_str + '.' for active_str in active_strs]
            hashes = [active_str + '#' for active_str in active_strs]
            active_strs = dots + hashes
            dots = []
            hashes = []
            for active_str in active_strs:
                if str_checker(active_str, spr_key):
                    checked_strs.append(active_str)
            active_strs = checked_strs
            checked_strs = []
    valid_count = 0
    for active_str in active_strs:
        if final_check(active_str, spr_key):
            valid_count += 1
    return valid_count

def str_checker(spr_str, spr_key):
    spr_str = spr_str.lstrip('.')
    break_count = 0
    key_index = 0
    spr_key.append(0)
    for spr in spr_str:
        if spr == '#':
            break_count += 1
            if break_count > spr_key[key_index]:
                return False
        elif spr == '.':
            if break_count > 0:
                if break_count != spr_key[key_index]:
                    return False
                key_index += 1
                break_count = 0
    return True

def final_check(spr_str, spr_key):
    if spr_str.count('#') == sum(spr_key):
        return True
    return False

def main():
    spr_strs, spr_keys = get_input()
    part1 = 0
    for index in range(len(spr_strs)):
        part1 += repair_checker(spr_strs[index], spr_keys[index])
    print(part1)

if __name__ == '__main__':
    main()