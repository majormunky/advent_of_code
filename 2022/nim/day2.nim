import strutils
import std/strformat


proc convert_to_object(letter: string): string =
    if letter == "X" or letter == "A":
        result = "Rock"
    elif letter == "Y" or letter == "B":
        result = "Paper"
    else:
        result = "Scissors"


proc get_score_for_selection(selection: string): int =
    if selection == "Rock": # Rock
        result = 1
    elif selection == "Paper": # Paper
        result = 2
    elif selection == "Scissors": # Scissors
        result= 3


proc get_score_for_game(opponent: string, your_selection: string): int =
    if opponent == "Rock":
        if your_selection == "Paper":
            # you win
            result = 6
        elif your_selection == "Rock":
            result = 3
        else:
            result = 0
    elif opponent == "Paper":
        if your_selection == "Scissors":
            # you win
            result = 6
        elif your_selection == "Paper":
            result = 3
        else:
            result = 0
    elif opponent == "Scissors":
        if your_selection == "Rock":
            # you win
            result = 6
        elif your_selection == "Scissors":
            result = 3
        else:
            result = 0


proc convert_outcome(letter: string): string =
    if letter == "X":
        result = "Lose"
    elif letter == "Y":
        result = "Draw"
    else:
        result = "Win"


proc get_your_choice(opp_choice: string, outcome: string): string =
    if outcome == "Draw":
        result = opp_choice
    else:
        if opp_choice == "Rock":
            if outcome == "Lose":
                result = "Scissors"
            else:
                result = "Paper"
        elif opp_choice == "Paper":
            if outcome == "Lose":
                result = "Rock"
            else:
                result = "Scissors"
        elif opp_choice == "Scissors":
            if outcome == "Lose":
                result = "Paper"
            else:
                result = "Rock"



# var test_lines: seq[string] = @[]
# test_lines.add("A Y")
# test_lines.add("B X")
# test_lines.add("C Z")

let contents = readFile("../data/day2_data.txt").strip()
let lines = contents.splitLines()

proc part1(lines: seq[string]): int =
    for line in lines:
        let parts = line.split(" ")
        let opp_choice = convert_to_object(parts[0])
        let your_choice = convert_to_object(parts[1])
        result += get_score_for_selection(your_choice)
        result += get_score_for_game(opp_choice, your_choice)


proc part2(lines: seq[string]): int =
    for line in lines:
        let parts = line.split(" ")
        let opp_choice = convert_to_object(parts[0])
        let outcome = convert_outcome(parts[1])
        let your_choice = get_your_choice(opp_choice, outcome)

        result += get_score_for_selection(your_choice)
        result += get_score_for_game(opp_choice, your_choice)


let part1_answer = part1(lines)
echo fmt"Part 1: {part1_answer}"

let part2_answer = part2(lines)
echo fmt"Part 2: {part2_answer}"
