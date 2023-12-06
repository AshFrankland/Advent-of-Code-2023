from math import sqrt, floor, ceil

def get_input():
    input = 'Day_06_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.lstrip('TimeDistance: ').rstrip('\n'))
        time_strs = raw_input[0].split(' ')
        dist_strs = raw_input[1].split(' ')
        while '' in time_strs:
            time_strs.remove('')
        while '' in dist_strs:
            dist_strs.remove('')
        times = []
        dists = []
        r_time_str = ''
        r_dist_str = ''
        for time in time_strs:
            times.append(int(time))
            r_time_str += time
        for dist in dist_strs:
            dists.append(int(dist))
            r_dist_str += dist
        return times, dists, [int(r_time_str)], [int(r_dist_str)]

def get_margins(times, dists):
    margins = []
    for time in range(len(times)):
        marg_low = (-times[time] + sqrt((times[time] * times[time]) - (4 * dists[time])))/-2
        marg_hi = (-times[time] - sqrt((times[time] * times[time]) - (4 * dists[time])))/-2
        margins.append([ceil(marg_low), floor(marg_hi)])
        if (margins[time][0] * (times[time] - margins[time][0])) == dists[time]:
            margins[time][0] += 1
        if (margins[time][1] * (times[time] - margins[time][1])) == dists[time]:
            margins[time][1] -= 1
    count = 1
    for margin in margins:
        count *= margin[1] - margin[0] + 1
    print(count)

def main():
    times, dists, real_time, real_dist = get_input()
    get_margins(times, dists)
    get_margins(real_time, real_dist)

if __name__ == '__main__':
    main()