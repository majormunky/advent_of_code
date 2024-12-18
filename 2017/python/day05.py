import os
import common


def part1():
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file)

    done = False
    index = 0
    steps = 0

    test_data = [int(x) for x in data]

    while not done:
        try:
            jump_amount = int(test_data[index])
            if jump_amount == 0:
                # increment our current index and skip rest of loop
                test_data[index] += 1

                # increase our steps now that we know we are done in this loop
                steps += 1
            else:
                # remember old index
                old_index = index

                # jump to new spot
                index += jump_amount

                # increment old index location
                test_data[old_index] += 1

                # increase our steps now that we know we are done in this loop
                steps += 1
        except IndexError:
            # the answer is found when we get an index outside of our list
            done = True
    return steps


def part2():
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file)

    done = False
    index = 0
    steps = 0

    test_data = [int(x) for x in data]

    while not done:
        try:
            jump_amount = int(test_data[index])
            if jump_amount == 0:
                # increment our current index with new rules
                if jump_amount >= 3:
                    test_data[index] -= 1
                else:
                    test_data[index] += 1
                # increase our steps
                steps += 1
            else:
                # remember old index
                old_index = index

                # jump to new spot
                index += jump_amount

                # increment our old index location with new rules
                if jump_amount >= 3:
                    test_data[old_index] -= 1
                else:
                    test_data[old_index] += 1

                # increase our steps now that we know we are done in this loop
                steps += 1
        except IndexError:
            # the answer is found when we get an index outside of our list
            done = True
    return steps


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
