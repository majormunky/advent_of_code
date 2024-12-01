//
//  main.swift
//  AdventOfCode-Day1-2016
//
//  Created by Josh Bright on 11/30/20.
//

import Foundation

let test_puzzle_input = "R2, L3"

func get_distance(x: Int, y: Int) -> Int {
    return x + y
}

func get_new_direction(current: String, turn_direction: String) -> String {
    let result: String
    let directions = ["N", "W", "S", "E"]
    let dir_index = directions.firstIndex(of: current)!

    if turn_direction == "L" {
        if dir_index == 0 {
            result = directions[3]
        } else {
            result = directions[dir_index - 1]
        }
    } else {
        if dir_index == 3 {
            result = directions[0]
        } else {
            result = directions[dir_index + 1]
        }
    }

    return result
}

func part1() -> Int {
    var current_direction = "N"
    var x_pos = 0
    var y_pos = 0
    for item in test_puzzle_input.split(separator: ",") {
        var action = item.trimmingCharacters(in: .whitespaces)
        let direction = String(action.removeFirst())
        let steps = Int(action)!

        let new_direction = get_new_direction(current: current_direction, turn_direction: direction)

        switch new_direction {
        case "N":
            y_pos += steps
        case "W":
            x_pos += steps
        case "S":
            y_pos -= steps
        case "E":
            x_pos -= steps
        default:
            print("Unknown new direction: \(new_direction)")
        }

        current_direction = String(new_direction)
    }

    let result = get_distance(x: x_pos, y: y_pos)
    return result
}

let part1_answer = part1()

print("Advent Of Code 2016: Day 1")
print("Part 1 Answer: \(part1_answer)")
