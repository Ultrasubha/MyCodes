package main

import (
	"fmt"
	"strings"
)

/*
	Basically Normal sentence = Subject - Verb - Object
				Yoda sentence  = Object - Subject - Verb
*/
func main() {
	sentence := "I must go party"
	s := strings.Split(sentence, " ")

	for i := 0; i < len(s); i++ {
		fmt.Println(s[i])
	}
}
