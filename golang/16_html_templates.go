package main

import ("fmt"
	"net/http"
	"html/template"
	"path/filepath"
	"os"
)

type NewsAppPage struct {
	Title string
	News string
}

func newsAgghandler(w http.ResponseWriter, r *http.Request)  {
	p := NewsAppPage{Title: "Amazing news agg", News: "some news!"}
	// From IntelliJ the following throws "no such file or directory"
	t, err := template.ParseFiles("basictemplating.html")
	fmt.Println(err)
	t.Execute(w,p)
}

func index_handler(w http.ResponseWriter, r *http.Request)  {
	fmt.Fprint(w, "<h1>Whoa, Go is neat!</h1>")
}

func main() {
	dir, _ := filepath.Abs(filepath.Dir(os.Args[0]))
	fmt.Println(dir)

	http.HandleFunc("/", index_handler)
	http.HandleFunc("/agg/", newsAgghandler)
	http.ListenAndServe(":8000", nil)
}
