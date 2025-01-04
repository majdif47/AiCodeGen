class WeatherForecast {
    constructor(city, apiKey) {
        this.city = city;
        this.apiKey = apiKey;
    }

    async getWeather() {
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${this.city}&appid=${this.apiKey}`);
        const weatherData = await response.json();
        
        if (weatherData.cod === '404') {
            throw new Error(`City '${this.city}' not found.`);
        }

        return weatherData;
    }
}

class WeatherApp {
    constructor(apiKey) {
        this.apiKey = apiKey;
    }

    async run(city) {
        const forecast = new WeatherForecast(city, this.apiKey);
        try {
            const weatherData = await forecast.getWeather();
            console.log(`Current Weather in ${city}:`);
            console.log(`Main: ${weatherData.weather[0].description}`);
            console.log(`Temp (Celsius): ${weatherData.main.temp}`);
            console.log(`Temp (Fahrenheit): ${(weatherData.main.temp - 273.15) * 9 / 5}.`);
        } catch (error) {
            console.error(error.message);
        }
    }
}

// Usage
const apiKey = 'your_openweathermap_api_key';
const weatherApp = new WeatherApp(apiKey);
weatherApp.run('London');
