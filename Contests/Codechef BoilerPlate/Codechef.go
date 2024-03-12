package main

import (
	"fmt"
)

func main() {
	var TestCase int
	fmt.Scanln(&TestCase)

	for ; TestCase > 0; TestCase-- {
		code()
	}
}

func code() {
	var N int
	fmt.Scanln(&N)

	var elem, sum int
	sum = 0
	for lim := 2*N - 1; lim > 0; lim-- {
		fmt.Scanf("%d", &elem)
		sum += elem
	}
	fmt.Scanf("%d\n", &elem)
	sum += elem

	switch {
	case sum%2 == 0:
		fmt.Println("YES")
	default:
		fmt.Println("NO")
	}
}
