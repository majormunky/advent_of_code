package utils

import (
	"bufio"
	"os"
)

func GetFileLines(filename string) ([]string, error) {
	f, err := os.Open(filename)
	if err != nil {
		return nil, err
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var result []string

	for scanner.Scan() {
		line := scanner.Text()

		result = append(result, line)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return result, nil
}
