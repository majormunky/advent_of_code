//
//  main.swift
//  day01
//
//  Created by Josh Bright on 3/18/24.
//

import Foundation

extension Sequence where Element: AdditiveArithmetic {
    func sum() -> Element { reduce(.zero, +) }
}

extension Character {
    func asInt() -> Int? {
        guard self.isNumber else { return nil }
        guard let myNumber = NumberFormatter().number(from: String(self)) else { return nil }

        return myNumber.intValue
    }
}

var testStrings = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

var testStrings2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

let lines = getLines()
let answer_part1 = part1(data: lines)
print("Part 1: \(answer_part1)")

let answer_part2 = part2(data: lines)
print("Part 2: \(answer_part2)")

func getLines() -> [String] {
    let filePath = "../data/day01_input.txt"
    let fileContents = try? String(contentsOfFile: filePath)

    return fileContents?.components(separatedBy: .newlines) ?? []
}

func part1(data: [String]) -> Int {
    var values: [Int] = []

    for item in data {
        var rowValues: [Int] = []
        item.forEach { c in
            if let numValue = c.asInt() {
                rowValues.append(numValue)
            }
        }

        if rowValues.count > 0 {
            let intStr = "\(rowValues.first!)\(rowValues.last!)"
            if let intStr = NumberFormatter().number(from: intStr) {
                values.append(intStr.intValue)
            }
        }
    }

    return values.sum()
}

func process(line: String) -> Int? {
    let numberStrings = [
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    ]

    var numbers: [Int] = []

    for index in 0...line.count {
        let startIndex = line.index(line.startIndex, offsetBy: index)
        let subStr = line[startIndex..<line.endIndex]

        for (numString, numValue) in numberStrings {
            if subStr.hasPrefix(numString) {
                numbers.append(numValue)
            } else if subStr.hasPrefix("\(numValue)") {
                numbers.append(numValue)
            }
        }
    }

    let intStr = "\(numbers.first!)\(numbers.last!)"
    if let intStr = NumberFormatter().number(from: intStr) {
        return intStr.intValue
    }

    return nil
}

func part2(data: [String]) -> Int {
    var answer = 0

    for item in data {
        if item.count == 0 {
            continue
        }
        if let lineAnswer = process(line: item) {
            answer += lineAnswer
        }
    }

    return answer
}
