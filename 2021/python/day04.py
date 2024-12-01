import os
import common


class BingoBoard:
    def __init__(self, data):
        self.winning_number = 0
        self.completed = False
        self.lines = []
        for line in data:

            parts = line.split(" ")
            new_line = [x for x in parts if x != ""]

            self.lines.append(new_line)
        self.marked = [[False for _ in range(5)] for _ in range(5)]

    def check_number(self, num):
        for index, line in enumerate(self.lines):
            if num in list(line):
                num_index = line.index(num)
                try:
                    self.marked[index][num_index] = True
                except IndexError:
                    print("Bad index!", index, num_index)

    def check_board(self):
        for line in self.marked:
            if all(line):
                return True

        index_check = True
        for i in range(5):
            for line in self.marked:
                if not line[i]:
                    index_check = False

            if index_check:
                return True
        return index_check

    def get_score(self):
        score = 0
        for line_index, line in enumerate(self.marked):
            for col_index, col in enumerate(line):
                if col is False:
                    score += int(self.lines[line_index][col_index])
        return score * self.winning_number

    def print_board(self):
        output = []
        for line_index, line in enumerate(self.marked):
            line_output = ""
            for col_index, col in enumerate(line):
                num = self.lines[line_index][col_index]
                if col:
                    line_output += "[{}]".format(num)
                else:
                    line_output += " {} ".format(num)
            output.append(line_output)
        for output_line in output:
            print(output_line)


def build_boards(lines):
    result = []

    board = []
    for line in lines:
        if len(board) < 5:
            board.append(line)
        else:
            new_board = BingoBoard(board)
            result.append(new_board)
            board = []
    return result


def p1():
    real_file = os.path.join("..", "data", "day04_input.txt")
    data = common.get_file_contents(real_file)

    bingo_numbers = data.pop(0)
    data.pop(0)

    boards = build_boards(data)

    numbers_drawn = []

    winning_board = None

    for num in bingo_numbers.split(","):
        numbers_drawn.append(num)
        for board in boards:
            board.check_number(num)
            if board.check_board():
                board.winning_number = int(num)
                winning_board = board
                break
        else:
            continue
        break
    # print("Winner!")
    # winning_board.print_board()
    print()

    if winning_board:
        return winning_board.get_score()
    return 0


def p2():
    real_file = os.path.join("..", "data", "day04_input.txt")
    data = common.get_file_contents(real_file)

    bingo_numbers = data.pop(0)
    data.pop(0)

    boards = build_boards(data)

    numbers_drawn = []

    winning_boards = []

    for num in bingo_numbers.split(","):
        numbers_drawn.append(num)
        for board in boards:
            if board.completed == False:
                board.check_number(num)
                if board.check_board():
                    board.winning_number = int(num)
                    board.completed = True
                    winning_boards.append(board)

    score = winning_boards[-1].get_score()
    return score


if __name__ == "__main__":
    print("Part 1:", p1())
    print("Part 2:", p2())
