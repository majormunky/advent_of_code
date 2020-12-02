import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def part1():
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
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()

