import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def part1():
    field = []
    pos = [0, 0]
    tree_count = 0
    for row in data:
        field.append(list(row))

    print("Field Size:")
    print("Width:", len(field[0]))
    print("Height:", len(field))

    # loop until we are done
    while True:
        # check what the current spot is
        if field[pos[1]][pos[0]] == "#":
            # its a tree, increase our count
            tree_count += 1

            # for visuals, mark this as an x
            field[pos[1]][pos[0]] = "X"
        else:
            # we did not hit a tree
            # mark with a O for visuals
            field[pos[1]][pos[0]] = "O"

        # increase our position further down the field
        pos[0] += 3
        pos[1] += 1

        # if we reached the right side of the field
        # then we reset our position back to the start
        if pos[0] >= len(field[0]):
            pos[0] = pos[0] - len(field[0])

        # if we've reached the bottom of the field, we are done
        if pos[1] >= len(field):
            break
        
    # print out the field for fun
    for row in field:
        print("".join(row))

    return tree_count


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()

