package main

import (
    "fmt"
    "strings"
    "time"
)

// WeatherForecast holds current and forecasted weather conditions
type WeatherForecast struct {
    CurrentTemp float64 `json:"current_temp"`
    ForecastTemp float64 `json:"forecast_temp"`
}

// CityWeatherData provides city-specific weather information
type CityWeatherData struct {
    Location string   `json:"location"`
    Weather  WeatherForecast `json:"weather"`
}

func getCityWeatherData(location string) ([]CityWeatherData, error) {
    // Simulate fetching data from a public API (e.g., OpenWeatherMap)
    return []CityWeatherData{
        {
            Location: "New York",
            Weather: WeatherForecast{
                CurrentTemp: 22.0,
                ForecastTemp: 25.0,
            },
        },
        {
            Location: "London",
            Weather: WeatherForecast{
                CurrentTemp: 18.0,
                ForecastTemp: 20.0,
            },
        },
    }, nil
}

func main() {
    // Example usage:
    locations := []string{"New York", "Los Angeles", "Paris"}
    for _, location := range locations {
        weatherData, err := getCityWeatherData(location)
        if err != nil {
            fmt.Printf("Error fetching weather data for %s: %v\n", location, err)
            continue
        }
        for _, data := range weatherData {
            fmt.Printf("Location: %s\nCurrent Temp: %.2f°C\nForecast Temp: %.2f°C\n", data.Location, data.Weather.CurrentTemp, data.Weather.ForecastTemp)
            time.Sleep(1 * time.Second) // Simulate delay between API requests
        }
    }
}
