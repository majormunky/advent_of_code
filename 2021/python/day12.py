import collections
from common import get_file_contents

# import time


def build_graph(lines):
    edges = collections.defaultdict(set)
    for line in lines:
        left, right = line.split("-")
        edges[left].add(right)
        edges[right].add(left)
    return edges


def p1():
    lines = get_file_contents("data/day12_input.txt")
    edges = build_graph(lines)

    todo = [("start",)]
    all_paths = set()

    while todo:
        path = todo.pop()
        print(path)
        if path[-1] == "end":
            all_paths.add(path)
            continue
        for edge in edges[path[-1]]:
            if not edge.islower() or edge not in path:
                todo.append((*path, edge))

    print(len(all_paths))


def p2():
    lines = get_file_contents("data/day12_input.txt")
    edges = build_graph(lines)

    todo = [("start",)]
    all_paths = set()
    bad_paths = set()
    ticks = 0

    while todo:
        ticks += 1
        path = todo.pop()
        # print(path)
        if path[-1] == "end":
            all_paths.add(path)
            # print("Adding Path")
            continue
        if path[-1] == "start" and len(path) > 1:
            # print("Adding Bad Path")
            bad_paths.add(path)
            continue
        for edge in edges[path[-1]]:
            if not edge.islower() or path.count(edge) < 2 and edge != "start":
                new_path = (*path, edge)
                if new_path not in bad_paths:
                    todo.append(new_path)
            else:
                bad_paths.add((*path, edge))

        if ticks % 1000 == 0:
            print(ticks, len(all_paths))

    print(len(all_paths))


def main():
    p2()


if __name__ == "__main__":
    main()
