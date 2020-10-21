# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    min_refills = 0
    num_of_stops = len(stops)
    # insert the whole distance at the end of stops
    stops.append(distance)
    # insert 0  at the beginning of stops
    stops.insert(0, 0)

    current_stop = 0
    can_go_upto = stops[0] + tank
    while current_stop <= num_of_stops:
        previous_can_go_upto = can_go_upto
        if stops[current_stop + 1] > can_go_upto:
            # refill here
            can_go_upto = stops[current_stop] + tank
            # if no moves are made then we can't go further than current_stop
            if can_go_upto == previous_can_go_upto:
                return -1
            min_refills += 1
        else:
            current_stop += 1
    return min_refills


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    num_of_stops = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))
