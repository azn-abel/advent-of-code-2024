package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func recur(curr int, remaining []int, goal int) bool {
	if len(remaining) == 0 {
		if curr == goal {
			return true
		}
		return false
	}

	return (recur(curr*remaining[0], remaining[1:], goal) ||
		recur(curr+remaining[0], remaining[1:], goal))
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	ans := 0

	for scanner.Scan() {
		var goal int
		nums := []int{}

		line := scanner.Text()
		chunks := strings.Split(line, ":")

		fmt.Sscanf(chunks[0], "%v", &goal)

		for _, s := range strings.Split(chunks[1][1:], " ") {
			num, _ := strconv.Atoi(s)
			nums = append(nums, num)
		}

		if recur(nums[0], nums[1:], goal) {
			ans += goal
		}

	}

	fmt.Println(ans)
}
