import os
import common


def get_winning_shape(target):
    if target == "rock":
        return "paper"
    elif target == "paper":
        return "scissors"
    elif target == "scissors":
        return "rock"


def get_losing_shape(target):
    if target == "rock":
        return "scissors"
    elif target == "paper":
        return "rock"
    elif target == "scissors":
        return "paper"


def handle_game(left, right):
    if left == "rock":
        if right == "paper":
            return "right"
        elif right == "scissors":
            return "left"
        else:
            return "same"
    elif left == "paper":
        if right == "rock":
            return "left"
        elif right == "scissors":
            return "right"
        else:
            return "same"
    elif left == "scissors":
        if right == "paper":
            return "left"
        elif right == "rock":
            return "right"
        else:
            return "same"


def get_shapes_from_line(line):
    rps = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    left, right = line.split(" ")
    left_actual = rps.get(left)
    right_actual = rps.get(right)
    return (left_actual, right_actual)


def get_data_from_line(line):
    left, right = get_shapes_from_line(line)
    game_status = None
    if right == "rock":
        game_status = "lose"
    elif right == "paper":
        game_status = "draw"
    elif right == "scissors":
        game_status = "win"
    return (left, game_status)


SCORES = {"rock": 1, "paper": 2, "scissors": 3}


def score_game_p1(lines):
    total_score = 0

    for line in lines:
        left_actual, right_actual = get_shapes_from_line(line)
        who_won = handle_game(left_actual, right_actual)

        this_game_score = SCORES.get(right_actual)

        if who_won == "right":
            # win bonus
            this_game_score += 6
        elif who_won == "same":
            # draw bonus
            this_game_score += 3

        message = f"Game of {left_actual} vs {right_actual}:"
        if who_won == "right":
            message += f" You win!  Game Score: {this_game_score}"
        elif who_won == "same":
            message += f" Ended in a draw.  Game Score: {this_game_score}"
        elif who_won == "left":
            message += " You lost.  Game Score: 0"
        print(message)
        total_score += this_game_score
    return total_score


def score_game_p2(lines):
    """
    X: Need to lose
    Y: Draw
    Z: Need to win

    """
    total_score = 0

    for line in lines:
        target, status = get_data_from_line(line)
        chosen_shape = None
        game_score = 0
        match status:
            case "lose":
                chosen_shape = get_losing_shape(target)
            case "draw":
                chosen_shape = target
                game_score += 3
            case "win":
                chosen_shape = get_winning_shape(target)
                game_score += 6
        game_score += SCORES.get(chosen_shape)
        total_score += game_score
    return total_score


def p1():
    """
    Score for a single round is:
        - Shape Score
            - 1 Rock
            - 2 Paper
            - 3 Scissors
        - Out come of round
            - 0 Loss
            - 3 Draw
            - 6 Win
    """
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)
    score = score_game_p1(lines)

    print("Score: ", score)


def p2():
    """
    This time the second character on each line is how the round ended
    instead of it being a specific shape
        X -> Lose
        Y -> Draw
        Z -> Win
    """
    # test_lines = [
    #     "A Y",
    #     "B X",
    #     "C Z",
    # ]
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)

    score = score_game_p2(lines)
    print(score)


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
