package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Move struct {
	r int
	c int
	d string
}

var dirs = map[string][]int{
	"^": {-1, 0},
	">": {0, 1},
	"<": {0, -1},
	"v": {1, 0},
}

var nextDir = map[string]string{
	"^": ">",
	">": "v",
	"<": "^",
	"v": "<",
}

var originalGrid = [130][130]string{}

func attempt(i, j int) bool {
	if originalGrid[i][j] == "^" || originalGrid[i][j] == "#" {
		return false
	}

	grid := [130][130]string{}
	for i, row := range originalGrid {
		for j := range row {
			grid[i][j] = originalGrid[i][j]
		}
	}

	grid[i][j] = "#"

	curr := "^"

	r := 59
	c := 62

	cache := map[Move]bool{}

	for {

		move := Move{r, c, curr}

		if _, ok := cache[move]; ok {
			return true
		}

		cache[move] = true

		val, _ := dirs[curr]

		x, y := val[0], val[1]
		r += x
		c += y

		if r >= 130 || r < 0 || c >= 130 || c < 0 {
			return false
		}

		nextTile := grid[r][c]

		if nextTile != "#" {
			continue
		}

		r -= x
		c -= y

		curr, _ = nextDir[curr]

	}
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	i := 0
	for scanner.Scan() {

		line := scanner.Text()
		for j, val := range strings.Split(line, "") {
			originalGrid[i][j] = val
		}
		i++
	}

	total := 0

	for i := 0; i < 130; i++ {
		for j := 0; j < 130; j++ {
			if attempt(i, j) {
				total++
			}
		}
	}

	fmt.Println(total)

}
