package main

import (
	"github.com/gin-gonic/gin"
	"fmt"
	"time"
)

func main() {
	r := gin.Default()

	r.GET("/ping", func(c *gin.Context) {
		// Print request time to console
		fmt.Println("Request time:", time.Now().Format(time.RFC3339))
		// Print all request headers to console
		for key, value := range c.Request.Header {
			fmt.Printf("%s: %s\n", key, value)
		}
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.Run(":8080") // Listen and serve on 0.0.0.0:8080
}
