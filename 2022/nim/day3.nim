import strutils
import sequtils
import sets
import strformat


proc getCodeForChar(s: char): int =
    var letters: seq[char] = @[]

    for asciiCode in 97..122:
        letters.add(chr(asciiCode))
    
    for asciiCode in 65..90:
        letters.add(chr(asciiCode))
    
    result = find(letters, s)
    result += 1


var test_lines: seq[string] = @[]
test_lines.add("vJrwpWtwJgWrhcsFMMfFFhFp")
test_lines.add("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
test_lines.add("PmmdzqPrVvPwwTWBwg")
test_lines.add("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
test_lines.add("ttgJtRGJQctTZtZT")
test_lines.add("CrZsJsPPZsGzwwsLwLmpwMDw")

let contents = readFile("data/day3_data.txt").strip()
let lines = contents.splitLines()

proc part1(lines: seq[string]): int =
    result = 0

    for line in lines:
        let line_length = len(line)
        let half_length = int(line_length / 2)

        let first_half = line[0 ..< half_length]
        let last_half = line[half_length ..< line_length]

        let first_list = toSeq(first_half.items)
        let last_list = toSeq(last_half.items)

        var first_set = toHashSet(first_list)
        var last_set = toHashSet(last_list)

        let common = first_set * last_set
        let remaining = toSeq(common)[0]
        let priority = getCodeForChar(remaining)
        result += priority


proc part2(lines: seq[string]): int =
    var grouped: seq[seq[string]] = @[]
    var temp_group: seq[string] = @[]
    for line in lines:
        temp_group.add(line)
        if len(temp_group) == 3:
            grouped.add(temp_group)
            temp_group = @[]
    
    for group in grouped:
        echo group

    result = 0



var part1_result = part1(lines)
echo fmt"Part 1: {part1_result}"

var part2_result = part2(test_lines)
echo fmt"Part 2: {part2_result}"
