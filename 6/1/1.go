package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	dirs := map[string][]int{
		"^": {-1, 0},
		">": {0, 1},
		"<": {0, -1},
		"v": {1, 0},
	}

	nextDir := map[string]string{
		"^": ">",
		">": "v",
		"<": "^",
		"v": "<",
	}

	grid := [][]string{}

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {

		line := scanner.Text()
		grid = append(grid, strings.Split(line, ""))

	}

	total := 1

	curr := "^"
	r := 59
	c := 62

	for {
		val, _ := dirs[curr]

		x, y := val[0], val[1]
		r += x
		c += y

		if r >= 130 || r < 0 || c >= 130 || c < 0 {
			break
		}

		nextTile := grid[r][c]

		if nextTile == "." {
			grid[r][c] = "X"
			total += 1
			continue
		}

		if nextTile == "X" {
			continue
		}

		r -= x
		c -= y

		curr, _ = nextDir[curr]

	}

	fmt.Println(total)

}
