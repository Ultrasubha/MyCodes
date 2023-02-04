package main

import "fmt"

func main() {
}

func makeArr(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size-1; i++ {
		fmt.Scanf("%d", &arr[i])
	}
	fmt.Scanf("%d\n", &arr[size-1])
	return arr
}
