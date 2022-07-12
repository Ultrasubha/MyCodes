package main

import (
	"fmt"
	"strings"
)

func main() {
	var TestCase int
	fmt.Scanln(&TestCase)

	for ; TestCase > 0; TestCase-- {
		code()
	}
}

func code() {
	var num int
	var s1 string
	fmt.Scanln(&num)
	fmt.Scanln(&s1)

	switch {
	case num%2 != 0:
		fmt.Println("YES")
	default:
		one := strings.Count(s1, "1")
		zero := strings.Count(s1, "0")

		switch {
		case one == zero || one%2 == 0:
			fmt.Println("YES")
		default:
			fmt.Println("NO")
		}
	}
}
