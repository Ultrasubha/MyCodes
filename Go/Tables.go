package main

import (
	"fmt"
	"strconv"
)

func main() {
	for num := 1; num <= 20; num++ {
		for upto := 1; upto <= 10; upto++ {
			val := num * upto
			s := strconv.Itoa(num) + " * " + strconv.Itoa(upto) + " = " + strconv.Itoa(val)
			fmt.Println(s)
		}
		fmt.Println("--------------")
	}
}
