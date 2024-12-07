package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {

	arr1 := []int{}
	arr2 := []int{}

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		var x1, x2 int

		line := scanner.Text()
		fmt.Sscanf(line, "%v %v", &x1, &x2)

		arr1 = append(arr1, x1)
		arr2 = append(arr2, x2)
	}

	sort.Ints(arr1)
	sort.Ints(arr2)

	ans := 0

	for i, val := range arr1 {
		other := arr2[i]
		temp := other - val
		if temp < 0 {
			ans -= temp
		} else {
			ans += temp
		}
	}

	fmt.Println(ans)
}
