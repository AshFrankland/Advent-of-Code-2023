import pprint

def get_input():
    input = 'Test_input.txt'
    #input = 'Day_01_input.txt'
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
    pass

def main():
    data_strings = get_input()
    #digit_finder(data_strings)
    print(data_strings)

if __name__ == '__main__':
    main()