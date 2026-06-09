package main

import (
	"encoding/csv"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
)

func main() {
apiKey := "b0b730e199f1d14cdca6f3ff6d22c4e3"

	// Create CSV file
    file, err := os.Create("TMDB_movies.csv")
	if err != nil {
    	panic(err)
	}
	defer file.Close()
    
    writer := csv.NewWriter(file)
    defer writer.Flush()
    
    // Write header
    writer.Write([]string{"Year", "Budget", "Revenue", "Genres"})
	// Loop through movie IDs
    for movieID := 1; movieID <= 5; movieID++ {
        url := fmt.Sprintf("https://api.themoviedb.org/3/movie/%d?api_key=%s", movieID, apiKey)
        
        resp, err := http.Get(url)
        if err != nil {
            fmt.Println("Error fetching movie", movieID, ":", err)
            continue
        }
        
        body, _ := ioutil.ReadAll(resp.Body)
        resp.Body.Close()
        
        var data map[string]interface{}
        json.Unmarshal(body, &data)
        
        // Check if movie, budget, and revenue exists
        if data["id"] == nil  && data["budget"] == nil && data["revenue"] == nil {
            continue
        }
    budget := fmt.Sprintf("%.0f", data["budget"].(float64))
    revenue := fmt.Sprintf("%.0f", data["revenue"].(float64))
    release_date := data["release_date"].(string)
	year := release_date[:4] // Get year only
    
    // Extract genres
        genresData := data["genres"].([]interface{})
        var genres string
        for i, g := range genresData {
            genre := g.(map[string]interface{})
            genres += genre["name"].(string)
            if i < len(genresData)-1 {
                genres += ", "
            }
        }

    
    // Write to CSV
        writer.Write([]string{year, budget, revenue, genres})
        
        fmt.Printf("Added: %s\n", movieID)
}
}