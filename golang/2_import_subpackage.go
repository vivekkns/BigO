package main

import ("fmt"
	"math"
	"math/rand")

func foo() {
	fmt.Println("A number b/w 1 to 100", rand.Intn(100))
}

func main()  {
	foo()
	fmt.Println("Sqrt(4)=", math.Sqrt(4))

	// Capital letter funcs are exportable from a package
	// just importing math and math.rand.Intn => doesn't work ! (Unlike in Python)
}
