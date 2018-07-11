package main

import ("fmt"
	"encoding/xml"
	"net/http"
	"io/ioutil"
	"html/template"
	"sync"
)

var wg sync.WaitGroup

type SitemapIndex struct {
	Locations []string `xml:"sitemap>loc"`
}

type News struct {
	Titles []string `xml:"url>news>title"`
	Keywords []string `xml:"url>news>keywords"`
	Locations []string `xml:"url>loc"`
}

type NewsMap struct {
	Keyword string
	Location string
}

type NewsAppPage struct {
	Title string
	News map[string]NewsMap
}

func newsRoutine(c chan News, Location string)  {
	defer wg.Done()
	var n News
	resp, _ := http.Get(Location)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &n)
	resp.Body.Close()
	c <- n
}

func newsAgghandler( w http.ResponseWriter, r *http.Request)  {
	var s SitemapIndex

	news_map := make(map[string]NewsMap)
	resp, _ := http.Get("https://www.washingtonpost.com/news-sitemap-index.xml")
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &s)
	resp.Body.Close()
	queue := make(chan News, 30)
	for _, Location := range s.Locations{
		wg.Add(1)
		go newsRoutine(queue, Location)
	}
	wg.Wait()
	close(queue)

	for n := range queue {
		for idx := range n.Titles {
			news_map[n.Titles[idx]] = NewsMap{n.Keywords[idx], n.Locations[idx]}
		}
	}


	p := NewsAppPage{Title: "Amazing news agg", News: news_map}
	// From IntelliJ the following throws "no such file or directory"
	t, err := template.ParseFiles("newsaggtemplate.html")
	fmt.Println(err)
	fmt.Println(t.Execute(w,p))
}

func index_handler(w http.ResponseWriter, r *http.Request)  {
	fmt.Fprint(w, "<h1>Whoa, Go is neat!</h1>")
}

func main() {
	http.HandleFunc("/", index_handler)
	http.HandleFunc("/agg/", newsAgghandler)
	http.ListenAndServe(":8000", nil)

}
