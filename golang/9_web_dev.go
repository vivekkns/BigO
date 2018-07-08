package main

import ("fmt"
	"net/http")

func index_handler(w http.ResponseWriter, r *http.Request) {
	// Multi line string
	fmt.Fprint(w, `<h1> Hey there!</h1>
	<p>Go is fast...</p>
	<p>and powerful!</p>`)
}

func main(){
	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":8000", nil)
}
