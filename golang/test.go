package main

import "fmt"

func main()  {
	fmt.Println("Hello !")

	i := 3
	switch {
	case i == 2, i == 1:
		fmt.Println("yes!")
	default:
		fmt.Println("no!")
	}
}
