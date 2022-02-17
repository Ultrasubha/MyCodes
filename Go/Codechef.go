//Coded By Subhadeep Mandal on 17th Feb 2022
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
	//Initialising
	var people, busSmoke, carSmoke, totalSmoke int
	fmt.Scanf("%d %d %d\n", &people, &busSmoke, &carSmoke)

	switch {
	case busSmoke < carSmoke: //Always Bus preffered no question asked
		bus := people / 100
		if (bus == 0) || (people%100 > 0) {
			bus++
		}
		totalSmoke = bus * busSmoke

	default:
		totalSmoke = smokeOut(people, busSmoke, carSmoke)

		if onlyCarSmoke(people, carSmoke) < totalSmoke {
			totalSmoke = onlyCarSmoke(people, carSmoke)
		}
	}

	fmt.Println(totalSmoke)
}

func onlyCarSmoke(people, carSmoke int) int {
	car := people / 4
	if (people % 4) > 0 {
		car++
	}
	return car * carSmoke
}

func smokeOut(people, busSmoke, carSmoke int) int {
	var smoke int
	bus := people / 100
	remCarSmoke := substituteCars(people) * carSmoke

	if remCarSmoke < busSmoke {
		smoke = bus*busSmoke + remCarSmoke
	} else {
		smoke = bus*busSmoke + busSmoke
	}
	return smoke
}

func substituteCars(people int) int {
	var car int
	rem := people % 100
	if rem != 0 {
		car = rem / 4
		if rem%4 > 0 {
			car++
		}
	}
	return car
}
