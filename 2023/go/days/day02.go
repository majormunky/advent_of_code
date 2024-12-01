package days

import (
	"log"
	"strings"

	"joshbright.dev/aoc/utils"
)

type game struct {
	name     string
	gameList []map[string]int
}

func generateGame(line string) game {
	// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
	parts := strings.Split(line, ":")
	gameName := parts[0]

	result := game{
		name: gameName,
	}

	gameParts = strings.Split(parts[1], ";")

	for _, gp := range gameParts {
		gameData := map[string]int{}

	}

}

func Day02Part1() {
	lines, err := utils.GetFileLines("../data/day02_input.test")
	if err != nil {
		log.Fatal(err)
	}

}

func Day02Part2() {

}
