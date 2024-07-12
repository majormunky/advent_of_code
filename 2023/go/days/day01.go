package days

import (
	"fmt"
	"log"
	"strconv"
	"strings"
	"unicode"

	"joshbright.dev/aoc/utils"
)

func process_line_part1(line string) int {
	var numbers []byte
	for index, char := range line {
		if unicode.IsDigit(char) {
			numbers = append(numbers, line[index])
		}
	}

	result := fmt.Sprintf("%c%c", numbers[0], numbers[len(numbers)-1])
	i, err := strconv.Atoi(result)

	if err != nil {
		return 0
	}

	return i
}

func process_line_part2(line string) int {
	var numbers []byte
	// Create mapping between number words and values
	numbersAsStrings := map[string]byte{
		"one":   '1',
		"two":   '2',
		"three": '3',
		"four":  '4',
		"five":  '5',
		"six":   '6',
		"seven": '7',
		"eight": '8',
		"nine":  '9',
	}

	// loop over the index for the length of the line
	for index, char := range line {

		// is this character a digit, if so, we can store it
		if unicode.IsDigit(char) {
			numbers = append(numbers, line[index])
		} else {
			// otherwise, check if the substring starts with a number word
			// we do this by looping over our map of number words
			for key, value := range numbersAsStrings {
				// and checking if our sub string starts with a number word
				if strings.HasPrefix(line[index:], key) {
					// and storing if it does
					numbers = append(numbers, value)
				}
			}
		}
	}

	result := fmt.Sprintf("%c%c", numbers[0], numbers[len(numbers)-1])
	i, err := strconv.Atoi(result)

	if err != nil {
		return 0
	}

	return i
}

func processDay(filepath string, transform func(string) int) int {
	lines, err := utils.GetFileLines(filepath)
	answer := 0

	if err != nil {
		log.Fatal(err)
	}

	for _, line := range lines {
		result := transform(line)
		answer += result
	}

	return answer
}

func Day01Part1() int {
	answer := processDay("data/day01_input.txt", process_line_part1)
	return answer
}

func Day01Part2() int {
	answer := processDay("data/day01_input.txt", process_line_part2)
	return answer
}
