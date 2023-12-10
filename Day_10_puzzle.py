from pprint import pprint

def get_input():
    input = 'test_input.txt'
    #input = 'Day_10_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        return raw_input

def main():
    get_input()

if __name__ == '__main__':
    main()