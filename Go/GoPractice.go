package main

import "fmt"

type Contact struct {
	name string
	age  int
}

func main() {
	x := make([]int, 5)
	x[1] = 2
	x[2] = 3

	for i := range x {
		fmt.Println(x[i])
	}
}

func (c Contact) getAge() int {
	return c.age
}
