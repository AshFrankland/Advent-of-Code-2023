def get_input():
    input = 'Day_10_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        pipe_map = {}
        start = ()
        row_ord = 0
        HEIGHT = len(raw_input)
        WIDTH = len(raw_input[0])
        for row in raw_input:
            col_ord = 0
            for col in row:
                if col == 'S':
                    start = (col_ord, row_ord)
                pipe_map[(col_ord, row_ord)] = col
                col_ord += 1
            row_ord += 1
        return pipe_map, start, HEIGHT, WIDTH

def second_pipe(pipe_map, start):
    if (start[0] + 1, start[1]) in pipe_map:
        if pipe_map[(start[0] + 1, start[1])] in ('-', 'J', '7'):
            return (start[0] + 1, start[1]), 'r'
        elif pipe_map[(start[0], start[1] + 1)] in ('|', 'J', 'L'):
            return (start[0], start[1] + 1), 'd'
        elif pipe_map[(start[0] - 1, start[1])] in ('-', 'L', 'F'):
            return (start[0] - 1, start[1]), 'l'
        else:
            return (start[0], start[1] - 1), 'u'

def follow_pipe(pipe_map, start):
    current_ord = start
    next_ord, map_dir = second_pipe(pipe_map, start)
    loop_len = 1
    loop_pipes = {}
    while pipe_map[next_ord] != 'S':
        loop_pipes[current_ord] = pipe_map[current_ord]
        current_ord = next_ord
        loop_len += 1
        if map_dir == 'r':
            if pipe_map[current_ord] == '-':
                next_ord = (current_ord[0] + 1, current_ord[1])
                map_dir = 'r'
            elif pipe_map[current_ord] == '7':
                next_ord = (current_ord[0], current_ord[1] + 1)
                map_dir = 'd'
            elif pipe_map[current_ord] == 'J':
                next_ord = (current_ord[0], current_ord[1] - 1)
                map_dir = 'u'
        elif map_dir == 'd':
            if pipe_map[current_ord] == '|':
                next_ord = (current_ord[0], current_ord[1] + 1)
                map_dir = 'd'
            elif pipe_map[current_ord] == 'L':
                next_ord = (current_ord[0] + 1, current_ord[1])
                map_dir = 'r'
            elif pipe_map[current_ord] == 'J':
                next_ord = (current_ord[0] - 1, current_ord[1])
                map_dir = 'l'
        elif map_dir == 'l':
            if pipe_map[current_ord] == '-':
                next_ord = (current_ord[0] - 1, current_ord[1])
                map_dir = 'l'
            elif pipe_map[current_ord] == 'F':
                next_ord = (current_ord[0], current_ord[1] + 1)
                map_dir = 'd'
            elif pipe_map[current_ord] == 'L':
                next_ord = (current_ord[0], current_ord[1] - 1)
                map_dir = 'u'
        elif map_dir == 'u':
            if pipe_map[current_ord] == '|':
                next_ord = (current_ord[0], current_ord[1] - 1)
                map_dir = 'u'
            elif pipe_map[current_ord] == 'F':
                next_ord = (current_ord[0] + 1, current_ord[1])
                map_dir = 'r'
            elif pipe_map[current_ord] == '7':
                next_ord = (current_ord[0] - 1, current_ord[1])
                map_dir = 'l'
    loop_pipes[current_ord] = pipe_map[current_ord]
    print(loop_len // 2)
    return loop_pipes

def scan_loop(loop_pipes, HEIGHT, WIDTH):
    on_loop = False
    area = 0
    for row in range(HEIGHT):
        in_out = False
        for col in range(WIDTH):
            if (col, row) in loop_pipes:
                if not on_loop:
                    on_loop = True
                    on_pipe = loop_pipes[(col, row)]
                    if on_pipe == '|':
                        in_out = not in_out
                        on_loop = False
                else:
                    if on_pipe == 'F' and loop_pipes[(col, row)] == 'J':
                        in_out = not in_out
                        on_loop = False
                    elif on_pipe == 'L' and loop_pipes[(col, row)] == '7':
                        in_out = not in_out
                        on_loop = False
                    elif on_pipe == 'F' and loop_pipes[(col, row)] == 'S':
                        in_out = not in_out
                        on_loop = False
                    elif on_pipe == 'F' and loop_pipes[(col, row)] == '7':
                        on_loop = False
                    elif on_pipe == 'L' and loop_pipes[(col, row)] == 'J':
                        on_loop = False
            else:
                if in_out:
                    area += 1
    print(area)

def main():
    pipe_map, start, HEIGHT, WIDTH = get_input()
    loop_pipes = follow_pipe(pipe_map, start)
    scan_loop(loop_pipes, HEIGHT, WIDTH)

if __name__ == '__main__':
    main()