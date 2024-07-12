package main

import (
	"fmt"
	"os"
	"reflect"

	"joshbright.dev/aoc/days"
)

func runFunction(functionName string) {
	funcMap := map[string]interface{}{
		"Day01Part1": days.Day01Part1,
		"Day01Part2": days.Day01Part2,
	}

	fn := reflect.ValueOf(funcMap[functionName])
	if fn.IsValid() {
		result := fn.Call(nil)
		fmt.Printf("%v: %v\n", functionName, result[0])
	}
}

func main() {
	args := os.Args[1:]

	funcName1 := fmt.Sprintf("%vPart1", args[0])
	funcName2 := fmt.Sprintf("%vPart2", args[0])

	runFunction(funcName1)
	runFunction(funcName2)
}
