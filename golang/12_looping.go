package main

import ("fmt"
	"encoding/xml"
	"net/http"
	"io/ioutil"
)

type Location struct {
	Loc string `xml:"loc"`
}

type SitemapIndex struct {
	Locations []Location `xml:"sitemap"`
}

func (l Location) String() string {
	return fmt.Sprintf(l.Loc)
}


func main() {
	for i:=0; i<10; i++{
		fmt.Println(i)
	}

	// While loop
	j := 0
	for j<10 {
		fmt.Println(j)
		j+=5
	}

	count := 1
	// Infinite loop
	for {
		fmt.Println(count, "hello")
		count++
		if count > 10 {
			break
		}
	}

	resp, _ := http.Get("https://www.washingtonpost.com/news-sitemap-index.xml")
	bytes, _ := ioutil.ReadAll(resp.Body)
	var s SitemapIndex
	xml.Unmarshal(bytes, &s)

	for _, Location := range s.Locations{
		fmt.Printf("\n%s", Location)
	}
}
