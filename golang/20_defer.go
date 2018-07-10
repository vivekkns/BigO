package main

import ("time"
	"fmt"
	"sync"
)

func foo() {
	// Panic handling can be done in defer
	// defer is called whether func executes successfully or not
	defer fmt.Println("defer test\n")
	defer fmt.Println("there")
	for i:=0; i < 5; i++{
		defer fmt.Println(i)
	}
	fmt.Println("Test")
}

var wg sync.WaitGroup

func say(s string){
	defer wg.Done()
	for i := 0; i < 3; i++ {
		fmt.Println(s)
		time.Sleep(time.Millisecond * 100)
	}
	// What if statements above errors/panics out?
	//wg.Done()
}

func main() {
	foo()
	wg.Add(1)
	go say("Hey")
	wg.Add(1)
	go say("There")
	wg.Wait()
}
