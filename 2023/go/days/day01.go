package days

import (
	"fmt"
	"log"
	"strconv"
	"unicode"

	"joshbright.dev/aoc/utils"
)

func process_line(line string) (int, error) {
	var numbers []byte
	for index, char := range line {
		if unicode.IsDigit(char) {
			numbers = append(numbers, line[index])
		}
	}

	result := fmt.Sprintf("%c%c", numbers[0], numbers[len(numbers)-1])
	i, err := strconv.Atoi(result)

	if err != nil {
		return 0, err
	}

	return i, nil
}

func Day01Part1() int {
	lines, err := utils.GetFileLines("data/day01_input.txt")
	answer := 0

	if err != nil {
		log.Fatal(err)
	}

	for _, line := range lines {
		// fmt.Println(line)
		result, err := process_line(line)
		if err != nil {
			log.Fatal(err)
		}

		answer += result
	}

	return answer
}
