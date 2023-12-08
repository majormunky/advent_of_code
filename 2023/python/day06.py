import time
import operator
import functools


test_data = ["Time:7 15 30", "Distance: 9 40 200"]
real_data = ["Time: 46 85 75 82", "Distance: 208 1412 1257 1410"]


def parse_lines(lines):
    result = []

    data_type = None
    for line in lines:
        line_parts = line.split(":")

        data_type = line_parts[0]

        for index, data_point in enumerate(line_parts[1].strip().split(" ")):
            if data_type == "Time":
                result.append([int(data_point), None])
            else:
                result[index][1] = int(data_point)

    return result


def process_race(race_time, distance):
    result = []

    hold_time = 1
    is_faster = False

    while True:
        # print("hold time", hold_time)
        travel_time = race_time - hold_time
        # print("travel time", travel_time)
        distance_travelled = travel_time * hold_time
        # print("distance_travelled", distance_travelled)
        if distance_travelled > distance:
            result.append(hold_time)
            is_faster = True
            # print("FASTER")
        else:
            if is_faster:
                break
        hold_time += 1
        # time.sleep(1)
        # print("")

    return result


def get_answer(num_list):
    accum_value = functools.reduce(operator.mul, num_list)
    return accum_value


def part1(debug=True):
    if debug:
        lines = test_data
    else:
        lines = real_data

    data = parse_lines(lines)

    time_data = []

    for race_data in data:
        race_time, distance = race_data
        result = process_race(race_time, distance)
        time_data.append(len(result))

    answer = get_answer(time_data)
    print(answer)


def part2(debug=True):
    if debug:
        lines = [71530, 940200]
    else:
        lines = [46857582, 208141212571410]

    time_data = []

    race_time, distance = lines
    result = process_race(race_time, distance)

    print(len(result))


if __name__ == "__main__":
    part1(False)
    part2(False)
