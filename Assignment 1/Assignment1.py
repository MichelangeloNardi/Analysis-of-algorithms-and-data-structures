import sys
from bisect import bisect_left

data = sys.stdin.read()

lines = data.splitlines()

test_cases = int(lines[0])

for test_case in range(test_cases):
    n_days = int(lines[1 + 4*test_case])
    available_days = list(map(int, lines[2 + 4*test_case].split()))
    n_customers = int(lines[3 + 4*test_case])
    desired_days = list(map(int, lines[4 + 4*test_case].split()))


### brute force approach

    # best_days = []

    # for day in desired_days:
    #     # find closest day if not equal
    #     best_index = 0
    #     min_gap = 10000000
    #     for available_day in available_days:
    #         gap = abs(day - available_day)
    #         if gap < min_gap:
    #             min_gap = gap
    #             best_day = available_day
        
    #     best_days.append(best_day)

    # output_str = " ".join(map(str, best_days))
    # print(output_str)

### sorting and binary search apporach 

    best_days = []
    available_days = sorted(available_days)
    for day in desired_days:
        pos = bisect_left(available_days, day)

        if pos == 0:
            best_day = available_days[0]
        elif pos == len(available_days):
            best_day = available_days[-1]
        else:
            before = available_days[pos - 1]
            after = available_days[pos]
        
            if abs(day - before) <= abs(day - after):
                best_day = before
            else:
                best_day = after

        best_days.append(best_day)

    # output_str = " ".join(map(str, best_days))
    for best_day in best_days:
        print(best_day)

