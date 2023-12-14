def get_input():
    input = 'Day_11_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        map_vert = []
        map_hori = []
        for space in range(len(raw_input)):
            map_vert.append('.')
        for space in range(len(raw_input[0])):
            map_hori.append('.')
        gal_dict = {}
        gal_count = 1
        for row in range(len(raw_input)):
            for col in range(len(raw_input[0])):
                if raw_input[row][col] == '#':
                    gal_dict[gal_count] = (col, row)
                    gal_count += 1
                    map_hori[col] = '#'
                    map_vert[row] = '#'
        return gal_dict, map_hori, map_vert, gal_count - 1

def find_dists(gal_dict, map_hori, map_vert, gal_count):
    total_dists1 = 0
    total_dists2 = 0
    for gal1 in range(1, gal_count):
        for gal2 in range(gal1 + 1, gal_count + 1):
            dist1 = 0
            dist2 = 0
            col = gal_dict[gal1][0]
            while col != gal_dict[gal2][0]:
                if gal_dict[gal1][0] < gal_dict[gal2][0]:
                    col += 1
                else:
                    col -= 1
                if map_hori[col] == '#':
                    dist1 += 1
                    dist2 += 1
                else:
                    dist1 += 2
                    dist2 += 1000000
            row = gal_dict[gal1][1]
            while row != gal_dict[gal2][1]:
                row += 1
                if map_vert[row] == '#':
                    dist1 += 1
                    dist2 += 1
                else:
                    dist1 += 2
                    dist2 += 1000000
            total_dists1 += dist1
            total_dists2 += dist2
    print(total_dists1)
    print(total_dists2)

def main():
    gal_dict, map_hori, map_vert, gal_count = get_input()
    find_dists(gal_dict, map_hori, map_vert, gal_count)

if __name__ == '__main__':
    main()