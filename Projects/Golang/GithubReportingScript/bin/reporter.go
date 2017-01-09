package main

import ("fmt"
        "net/http"
        "io/ioutil"
        "encoding/json"
        "os"
        
       "models")

func main() {
    res, err := http.Get("https://api.github.com/users/ryannewman2828/repos")
    if err != nil{
        fmt.Println(err)
        os.Exit(1)
    }
    defer res.Body.Close()
    var repo []models.Repository
    data, err := ioutil.ReadAll(res.Body)
    bytes := []byte(data)
    
    json.Unmarshal(bytes, &repo)
    
    fmt.Println(repo[0])
}