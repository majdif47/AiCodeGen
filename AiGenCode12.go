package main

import (
    "fmt"
    "math/rand"
    "time"
)

// Function to generate a realistic weather forecast for a given day
func GenerateWeatherForecast() string {
    var temperature, humidity, condition string
    rand.Seed(time.Now().UnixNano())

    // Randomly select temperature from a list of possible values
    temp := randomInt(20, 30)
    if rand.Intn(2) == 0 {
        temperature = fmt.Sprintf("%d°C", temp)
    } else {
        temperature = fmt.Sprintf("%d°F", temp)
    }

    // Generate humidity level (0-100%)
    humidityLevel := randomFloat(1, 101)

    // Randomly select weather condition
    conditions := []string{"Sunny", "Cloudy", "Rainy", "Snowy"}
    condition := conditions[rand.Intn(len(conditions))]

    return fmt.Sprintf("Today's forecast: %s, Humidity: %.0f%%, Condition: %s", temperature, humidityLevel, condition)
}

// Function to generate a list of random people
func GeneratePeopleList(numPeople int) []string {
    var people []string

    for i := 0; i < numPeople; i++ {
        firstNames := []string{"John", "Emily", "Michael", "Sophia", "William", "Olivia"}
        lastNames := []string{"Smith", "Johnson", "Williams", "Jones", "Brown", "Davis"}

        person := fmt.Sprintf("%s %s", randomString(firstNames), randomString(lastNames))
        people = append(people, person)
    }

    return people
}

// Function to generate a random string of length n from a given character set
func randomString(chars []string) string {
    var charsMap = map[rune]rune{
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
    }

    var randString string

    for i := 0; i < 5; i++ {
        char := rune(randomInt(97, 122)) // Generate a random lowercase letter
        if _, ok := charsMap[char]; !ok { // Check if the generated character is in our map
            continue
        }

        randString += string(char)
    }

    return randString
}

// Function to generate a random integer between min and max (inclusive)
func randomInt(min, max int) int {
    return min + rand.Intn(max-min+1)
}

// Function to generate a random float between min and max (inclusive)
func randomFloat(min, max float64) float64 {
    return min + float64(rand.Intn(int((max-min)*10)+1)) / 10
}

func main() {
    weatherForecast := GenerateWeatherForecast()
    fmt.Println(weatherForecast)

    peopleList := GeneratePeopleList(5)
    for _, person := range peopleList {
        fmt.Println(person)
    }
}
