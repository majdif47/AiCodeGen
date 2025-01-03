package main

import (
    "bytes"
    "fmt"
    "math/rand"
    "sync"
)

const (
    // Number of workers
    numWorkers = 5
    
    // Number of tasks to process
    numTasks = 10000
    
    // Maximum number of connections
    maxConnections = 10
    
    // Port to listen on
    port = 8080
)

var mu sync.Mutex
var count int

// Worker function that runs in a goroutine
func worker(id int) {
    for i := 0; i < numTasks; i++ {
        mu.Lock()
        count++
        mu.Unlock()
        fmt.Printf("Worker %d: Connection count is %d\n", id, count)
        time.Sleep(time.Second * 1)
    }
}

// Function to simulate connections
func simulateConnection() {
    time.Sleep(time.Second * 0.1)
}

func main() {
    // Seed random number generator
    rand.Seed(time.Now().UnixNano())

    var wg sync.WaitGroup

    // Start workers
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go worker(i)
    }

    // Simulate connections
    start := time.Now()
    mu.Lock()
    count = 0
    mu.Unlock()

    var mutex sync.Mutex

    for i := 0; i < maxConnections; i++ {
        go simulateConnection()
    }

    wg.Wait()
    end := time.Now()

    fmt.Printf("Time taken: %v\n", end.Sub(start))
}
