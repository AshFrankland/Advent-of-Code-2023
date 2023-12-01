def get_input():
    input = 'Day_01_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        return raw_input

def digit_finder(data_strings):
    index = 0
    scan_dir = 1
    digits = []
    for line in data_strings:
        digit = ''
        while True:
            if len(digit) == 2:
                index = 0
                scan_dir = 1
                break
            elif line[index].isnumeric():
                digit += line[index]
                index = -1
                scan_dir = -1
            else:
                index += scan_dir
        digits.append(int(digit))
    digit_sum = 0
    for num in digits:
        digit_sum += num
    print(digit_sum)

def num_finder(data_strings):
    num_names = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    index = 0
    scan_dir = 1
    nums = []
    for line in data_strings:
        num = ''
        check_str = ''
        while True:
            if len(num) == 2:
                index = 0
                scan_dir = 1
                break
            elif line[index].isnumeric():
                num += line[index]
                index = -1
                scan_dir = -1
                check_str = ''
            else:
                if scan_dir == 1:
                    check_str += line[index]
                else:
                    check_str = line[index] + check_str
                index += scan_dir
                if len(check_str) >= 3:
                    if num_names[1] in check_str:
                        num += '1'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    elif num_names[2] in check_str:
                        num += '2'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    elif num_names[6] in check_str:
                        num += '6'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                if len(check_str) >= 4:
                    if num_names[4] in check_str:
                        num += '4'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    elif num_names[5] in check_str:
                        num += '5'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    elif num_names[9] in check_str:
                        num += '9'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                if len(check_str) >= 5:
                    if num_names[3] in check_str:
                        num += '3'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    if num_names[7] in check_str:
                        num += '7'
                        index = -1
                        scan_dir = -1
                        check_str = ''
                    if num_names[8] in check_str:
                        num += '8'
                        index = -1
                        scan_dir = -1
                        check_str = ''
        nums.append(int(num))
    num_sum = 0
    for number in nums:
        num_sum += number
    print(num_sum)

def main():
    data_strings = get_input()
    digit_finder(data_strings)
    num_finder(data_strings)

if __name__ == '__main__':
    main()