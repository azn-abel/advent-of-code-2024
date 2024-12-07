package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	arr1 := []int{}
	similarity := make(map[int]int)

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		var x1, x2 int

		line := scanner.Text()

		fmt.Sscanf(line, "%v %v", &x1, &x2)
		arr1 = append(arr1, x1)

		val, ok := similarity[x2]
		if !ok {
			similarity[x2] = 1
		} else {
			similarity[x2] = val + 1
		}
	}

	ans := 0

	for _, val := range arr1 {
		if v, ok := similarity[val]; ok {
			ans += v * val
		}
	}

	fmt.Println(ans)
}
