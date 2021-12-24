// https://www.youtube.com/watch?v=WFFidtqPfhk&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=46&ab_channel=AprendaGo

package main

import "fmt"

func main() {
	x := 10

	switch {
	case x < 5:
		fmt.Println("X is less than 5")
	case x == 5:
		fmt.Println("X is equal to 5")
	case x > 5:
		fmt.Println("X is larger than 5")
	}

	quemtanoescritoriohoje := "marquinhos"
	switch quemtanoescritoriohoje {
	case "zezinho":
		fmt.Println("o zezinho tá no escritorio hoje")
	case "joana":
		fmt.Println("a joana tá no escritorio hoje")
	case "marquinhos":
		fmt.Println("o marquinhos tá no escritório hoje")
	default: // when none of the cases above is true, this is the default
		fmt.Println("o escritório tá vazio")
	}

	quemtanoescritoriohoje = "zezinho"
	switch quemtanoescritoriohoje {
	case "zezinho":
		fmt.Println("o zezinho tá no escritorio hoje")
		fallthrough
		// fallthrough is used to run the code below when the case above is true
	case "joana":
		fmt.Println("e sempre que o zezinho tá no escritório, a joana tbm tá")
	}

	quemtanoescritoriohoje = "pedrinho"
	switch quemtanoescritoriohoje {
	case "zezinho", "maria": // example of compound case switch
		fmt.Println("hoje quem tá no escritório é o time 1")
	case "pedrinho", "joana":
		fmt.Println("hoje quem tá na firma é o time 2")
	}

	x = 1
	switch x {
	case 1, 2:
		fmt.Println("1 or 2")
	case 3, 4:
		fmt.Println("3 or 4")
	}

	x = 8
	switch {
	case (x == 1), (x == 2):
		fmt.Println("1 or 2")
	case (x > 10):
		fmt.Println("x > 10")
	}
}

// next video
