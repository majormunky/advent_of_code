import strutils
import std/algorithm

let contents = readFile("data/day1_data.txt").strip()
let lines = contents.splitLines()

proc part1(lines: seq[string]): int =
    var current_elf = 0
    var heavy_elf = 0

    for line in lines:
        if line == "":
            if current_elf > heavy_elf:
                heavy_elf = current_elf
            current_elf = 0
            continue

        let line_as_int = parseInt(line)
        current_elf += line_as_int

    result = heavy_elf


proc part2(lines: seq[string]): int = 
    var current_elf = 0
    var elf_list: seq[int] = @[]

    for line in lines:
        if line == "":
            elf_list.add(current_elf)
            current_elf = 0
            continue

        let line_as_int = parseInt(line)
        current_elf += line_as_int

    elf_list.sort(order = SortOrder.Descending)
    result = elf_list[0] + elf_list[1] + elf_list[2]


echo part1(lines)
echo part2(lines)
