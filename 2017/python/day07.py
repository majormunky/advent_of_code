import os
import common


test_data = [
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)",
]


def get_row_key(row):
    return row.split(" ")[0]


def get_row_children(row):
    # vfosh (261) -> aziwd, tubze, dhjrv

    parts = row.split("->")
    parts = parts[1].split(", ")
    return [x.strip() for x in parts]


def part1():
    real_file = os.path.join("..", "data", "day07_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    answer = None
    nodes = []
    keys = []

    for row in data:
        # we are only interested in nodes with children
        if "->" in row:
            # find our row key, one of them is going to be our root node
            row_key = get_row_key(row)

            # get a list of the children of this node
            row_children = get_row_children(row)

            # add them to a list of all children nodes found
            nodes += row_children

            # add our key to a list to check later
            keys.append(row_key)

    # now that we have all the children, we can check our parent keys
    for rk in keys:
        # our root node should not be in the child list
        if rk not in nodes:
            answer = rk

    return answer


def part2():
    # real_file = os.path.join("..", "data", "day07_input.txt")
    # data = common.get_file_contents(real_file, single_line=True)

    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
