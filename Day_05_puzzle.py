def get_input():
    input = 'Day_05_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        seeds_str = raw_input.pop(0)
        seeds_str = seeds_str.lstrip('seeds: ').split(' ')
        seeds = []
        for seed in seeds_str:
            seeds.append(int(seed))
        raw_input.pop(0)
        maps_dict = {}
        map_name = 0
        for line in raw_input:
            if 'map' in line:
                map_name += 1
                maps_dict[map_name] = {'src_ranges': [], 'mappings': []}
            elif line == '':
                pass
            else:
                dest, src, rng = line.split(' ')
                maps_dict[map_name]['src_ranges'].append((int(src), int(src) + int(rng) - 1))
                maps_dict[map_name]['mappings'].append(int(dest) - int(src))
        return seeds, maps_dict

def seed_mapper(seeds, maps_dict):
    locations = []
    for seed in seeds:
        location = map_seed(seed, maps_dict)
        locations.append(location)
    part1 = ''
    for num in locations:
        if not part1:
            part1 = num
        elif num < part1:
            part1 = num
    print(part1)

def map_seed(seed, maps_dict):
    for step in range(1, 8):
        for mapping in range(len(maps_dict[step]['mappings'])):
            if seed in range(maps_dict[step]['src_ranges'][mapping][0], maps_dict[step]['src_ranges'][mapping][1] + 1):
                seed += maps_dict[step]['mappings'][mapping]
                break
    return seed

def find_seed_ranges(seeds):
    seed_ranges = []
    for num in range(len(seeds)):
        if num % 2 == 0:
            seed_range = (seeds[num], seeds[num] + seeds[num + 1] - 1)
            seed_ranges.append(seed_range)
    return seed_ranges

def range_mapper(seed_ranges, maps_dict):
    location_ranges = []
    for seed_range in seed_ranges:
        soil_ranges = map_range(seed_range, maps_dict, 1)
        for soil_range in soil_ranges:
            fert_ranges = map_range(soil_range, maps_dict, 2)
            for fert_range in fert_ranges:
                water_ranges = map_range(fert_range, maps_dict, 3)
                for water_range in water_ranges:
                    light_ranges = map_range(water_range, maps_dict, 4)
                    for light_range in light_ranges:
                        temp_ranges = map_range(light_range, maps_dict, 5)
                        for temp_range in temp_ranges:
                            humid_ranges = map_range(temp_range, maps_dict, 6)
                            for humid_range in humid_ranges:
                                loc_ranges = map_range(humid_range, maps_dict, 7)
                                for range in loc_ranges:
                                    location_ranges.append(range)
    part2 = ''
    for range in location_ranges:
        if not part2:
            part2 = range[0]
        elif range[0] < part2:
            part2 = range[0]
    print(part2)

def map_range(seed_range, maps_dict, step):
    new_ranges = []
    for mapping in range(len(maps_dict[step]['mappings'])):
        map_start = maps_dict[step]['src_ranges'][mapping][0]
        map_end = maps_dict[step]['src_ranges'][mapping][1]
        if seed_range[0] <= map_end and seed_range[1] >= map_start:
            if seed_range[0] in range(map_start, map_end + 1) and seed_range[1] in range(map_start, map_end + 1):
                new_ranges.append((seed_range[0] + maps_dict[step]['mappings'][mapping], seed_range[1] + maps_dict[step]['mappings'][mapping]))
                seed_range = ()
                break
            elif seed_range[0] in range(map_start, map_end + 1):
                new_ranges.append((seed_range[0] + maps_dict[step]['mappings'][mapping], map_end + maps_dict[step]['mappings'][mapping]))
                seed_range = (map_end, seed_range[1])
            elif seed_range[1] in range(map_start, map_end + 1):
                new_ranges.append((map_start + maps_dict[step]['mappings'][mapping], seed_range[1] + maps_dict[step]['mappings'][mapping]))
                seed_range = (seed_range[0], map_start)
            else:
                new_ranges.append((map_start + maps_dict[step]['mappings'][mapping], map_end + maps_dict[step]['mappings'][mapping]))
                #print('WARNING EDGE CASE DETECTED')
    if seed_range:
        new_ranges.append(seed_range)
    if new_ranges == []:
        return [seed_range]
    else:
        return new_ranges

def main():
    seeds, maps_dict = get_input()
    seed_mapper(seeds, maps_dict)
    seed_ranges = find_seed_ranges(seeds)
    range_mapper(seed_ranges, maps_dict)

if __name__ == '__main__':
    main()