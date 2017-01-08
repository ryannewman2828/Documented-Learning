package main

import ("fmt"
       "models")

func main() {
    a := models.Owner{}
    a.Login = "test"
    fmt.Println(a.Login)
}