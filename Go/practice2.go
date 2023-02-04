package main

import (
	"fmt"
	"time"
)

//define the download() function
func download(s int, ch chan int) {
	val := s * (s + 1) / 2
	ch <- val
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)
	ch3 := make(chan int)

	var s1, s2, s3 int
	fmt.Scanln(&s1)
	fmt.Scanln(&s2)
	fmt.Scanln(&s3)

	go download(s1, ch1)
	go download(s2, ch2)
	go download(s3, ch3)

	fmt.Println(<-ch1 + <-ch2 + <-ch3)
	time.Sleep(50 * time.Millisecond)
}
