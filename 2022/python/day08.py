from common import get_file_contents


DEBUG = False


def get_tree_view_distances(x, y, forest):
    print_message(f"Checking Tree: {x}, {y}")
    # left check
    tree_height = int(forest[y][x])
    print_message(f"  Target Tree Height: {tree_height}")

    result = {
        "left": 0,
        "right": 0,
        "top": 0,
        "bottom": 0
    }

    # left check
    print_message("  Checking left of target tree")
    for tx in range(x - 1, -1, -1):
        tree_to_check = int(forest[y][tx])
        print_message(f"    Checking Tree at ({tx}, {y}) - Height: {tree_to_check}")
        result["left"] += 1
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from left")
            break

    print_message("  Checking right of target tree")
    # right check
    for tx in range(x + 1, len(forest[0])):
        tree_to_check = int(forest[y][tx])
        print_message(f"    Checking Tree at ({tx}, {y}) - Height: {tree_to_check}")
        result["right"] += 1
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from right")
            break

    print_message("  Checking above target tree")
    # top check
    for ty in range(y - 1, -1, -1):
        tree_to_check = int(forest[ty][x])
        print_message(f"    Checking Tree at ({x}, {ty}) - Height: {tree_to_check}")
        result["top"] += 1
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from top")
            break

    print_message("  Checking below target tree")
    # bottom check
    for ty in range(y + 1, len(forest)):
        tree_to_check = int(forest[ty][x])
        print_message(f"    Checking Tree at ({x}, {ty}) - Height: {tree_to_check}")
        result["bottom"] += 1
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from bottom")
            break

    return result


def check_tree_is_visible(x, y, forest):
    print_message(f"Checking Tree: {x}, {y}")
    # left check
    tree_height = int(forest[y][x])
    print_message(f"  Target Tree Height: {tree_height}")

    result = {
        "left": True,
        "right": True,
        "top": True,
        "bottom": True
    }

    # left check
    print_message("  Checking left of target tree")
    for tx in range(x - 1, -1, -1):
        tree_to_check = int(forest[y][tx])
        print_message(f"    Checking Tree at ({tx}, {y}) - Height: {tree_to_check}")
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from left")
            result["left"] = False
            break

    print_message("  Checking right of target tree")
    # right check
    for tx in range(x + 1, len(forest[0])):
        tree_to_check = int(forest[y][tx])
        print_message(f"    Checking Tree at ({tx}, {y}) - Height: {tree_to_check}")
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from right")
            result["right"] = False
            break

    print_message("  Checking above target tree")
    # top check
    for ty in range(y - 1, -1, -1):
        tree_to_check = int(forest[ty][x])
        print_message(f"    Checking Tree at ({x}, {ty}) - Height: {tree_to_check}")
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from top")
            result["top"] = False
            break

    print_message("  Checking below target tree")
    # bottom check
    for ty in range(y + 1, len(forest)):
        tree_to_check = int(forest[ty][x])
        print_message(f"    Checking Tree at ({x}, {ty}) - Height: {tree_to_check}")
        if tree_to_check >= tree_height:
            print_message("    Target tree is not visible from bottom")
            result["bottom"] = False
            break

    for k, v in result.items():
        print_message(f"   {k}: {v}")

    end_result = any([v for k, v in result.items()])
    print_message(f"  End Result: {end_result}")
    return end_result


def print_message(msg):
    if DEBUG:
        print(msg)


def p1():
    lines = get_file_contents("data/day08_input.txt")
    count = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if x == 0 or y == 0 or y == len(lines) or x == len(lines[0]):
                print_message(f"Skipping {x}, {y}")
                count += 1
                print_message(f"----- Count: {count}")
                continue
            if check_tree_is_visible(x, y, lines):
                count += 1

            print_message(f"----- Count: {count}")
    print(count)


def get_tree_score(tree_data):
    if DEBUG:
        print("Left", tree_data["left"])
        print("Right", tree_data["right"])
        print("Top", tree_data["top"])
        print("Bottom", tree_data["bottom"])
    return tree_data["left"] * tree_data["right"] * tree_data["top"] * tree_data["bottom"]


def p2():
    # lines = [
    #     "30373",
    #     "25512",
    #     "65332",
    #     "33549",
    #     "35390",
    # ]
    lines = get_file_contents("data/day08_input.txt")

    tree_score = None
    selected_tree = None
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            tree_visibility = get_tree_view_distances(x, y, lines)
            this_tree_score = get_tree_score(tree_visibility)
            print_message(f"Tree Visibility: {tree_visibility}")
            print_message(f"Tree Score: {this_tree_score}")
            if tree_score is None:
                tree_score = this_tree_score
                selected_tree = (x, y)
            else:
                if this_tree_score > tree_score:
                    tree_score = this_tree_score
                    selected_tree = (x, y)

    print_message(selected_tree)
    print(tree_score)


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
