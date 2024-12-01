//
//  day02.swift
//
//
//  Created by Josh Bright on 3/20/24.
//

import Foundation

extension String {
    func trimmed() -> String {
        self.trimmingCharacters(in: .whitespacesAndNewlines)
    }

    mutating func trim() {
        self = self.trimmed()
    }
}

let test_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

let test_lines2 = [
    "Game 13: 12 red, 6 green, 2 blue; 15 green, 2 red, 4 blue; 7 green, 1 red, 3 blue"
]

let test_rules = [
    "red": 12,
    "green": 13,
    "blue": 14,
]

func getLines() -> [String] {
    let filePath = "../data/day02_input.txt"
    let fileContents = try? String(contentsOfFile: filePath)

    return fileContents?.components(separatedBy: .newlines) ?? []
}

func parseGamePart(data: String) -> [String: Int]? {
    var result: [String: Int] = [:]

    let dataString = data.trimmed()
    let parts = dataString.components(separatedBy: ", ")

    for a_part in parts {
        let p = a_part.components(separatedBy: " ")
        guard p.count == 2 else { continue }
        guard let intStr = NumberFormatter().number(from: p[0]) else { continue }

        result[p[1]] = intStr.intValue
    }

    if result.isEmpty {
        return nil
    }

    return result
}

func parse(line: String) -> (id: Int, data: [String])? {
    let lineParts = line.components(separatedBy: ":")
    guard let gameId = lineParts.first else { return nil }
    guard let gameId = gameId.components(separatedBy: " ").last else { return nil }
    guard let gameId = NumberFormatter().number(from: gameId) else { return nil }
    guard var gameData = lineParts.last else { return nil }

    gameData.trim()

    let gameParts = gameData.components(separatedBy: ";")

    return (id: Int(truncating: gameId), data: gameParts)
}

func part1(data: [String]) -> Int {
    var answer = 0

    for line in data {
        guard let game = parse(line: line) else { continue }

        var isValid = true

        for gamePart in game.data {

            guard let gamePartData = parseGamePart(data: gamePart) else { continue }

            for (color, amount) in gamePartData {
                guard let ruleValue = test_rules[color] else { continue }
                if amount > ruleValue {
                    isValid = false
                }
            }
        }

        if isValid {
            answer += game.id
        }
    }

    return answer
}

func part2(data: [String]) -> Int {
    var answer = 0

    for line in data {
        guard let game = parse(line: line) else { continue }

    }

    return 42
}

let answer_part1 = part1(data: getLines())
print("Part 1: \(answer_part1)")
