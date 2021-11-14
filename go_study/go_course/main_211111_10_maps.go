// go run main.go

// exercice
package main

import "fmt"

func main() {
	fmt.Println("Hello World!")
	// https://www.coderedcorp.com/blog/golang-for-python-devs/
	// Maps are the equivalent to Python Dictionaries

	fruits := map[string]string{
		"a": "Apple",
		"b": "Banana",
		"c": "Cherry",
	}
	// fmt.Println(fruits)

	// how to access elements in a map
	word := fruits["a"]
	fmt.Println(word)

	// Assignment for map
	fruits["d"] = "Dragonfruit"
	fmt.Println(fruits)

	for key, value := range fruits {
		fmt.Printf("%v: %v\n", key, value)
	}

	fmt.Println("--------------------")

	updateFruits := map[string]string{
		"c": "Cantaloupe",
		"d": "Durian",
	}

	for key, _ := range updateFruits {
		fruits[key] = updateFruits[key]
	}

	for key, value := range fruits {
		fmt.Printf("%v: %v\n", key, value)
	}

}

// digital systems
