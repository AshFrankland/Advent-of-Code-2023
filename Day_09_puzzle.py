def get_input():
    input = 'Day_09_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        data_strs = []
        for line in raw_input:
            data_strs.append(line.split(' '))
        data_hist = []
        for line in data_strs:
            data_hist.append([])
            for num in line:
                data_hist[-1].append(int(num))
        return data_hist

def predict_next(data_hist):
    part1 = 0
    part2 = 0
    for line in data_hist:
        last_nums = []
        first_nums = []
        num_list = line
        while not all(num == 0 for num in num_list):
            last_nums.append(num_list[-1])
            first_nums.append(num_list[0])
            num_list = interpolate(num_list)
        prediction = 0
        while last_nums:
            prediction += last_nums[-1]
            last_nums.pop()
        part1 += prediction
        more_hist = 0
        while first_nums:
            more_hist = first_nums[-1] - more_hist
            first_nums.pop()
        part2 += more_hist
    print(part1)
    print(part2)

def interpolate(num_list):
    new_list = []
    for index in range(len(num_list) - 1):
        new_list.append(num_list[index + 1] - num_list[index])
    return new_list

def main():
    data_hist = get_input()
    predict_next(data_hist)

if __name__ == '__main__':
    main()