class WeatherTracker {
  constructor() {
    this.currentWeather = {};
    this.weatherHistory = [];
  }

  async getWeather(city) {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=YOUR_API_KEY`);
    if (response.ok) {
      this.currentWeather = await response.json();
      return this.currentWeather;
    } else {
      throw new Error('Failed to retrieve weather data');
    }
  }

  addWeatherEntry(city, temperature, condition) {
    const entry = { city, temperature, condition };
    this.weatherHistory.push(entry);
  }

  getWeatherHistory() {
    return this.weatherHistory.map((entry, index) => ({ ...entry, timestamp: new Date(`${Date.now()}${index}`) }));
  }
}

class WeatherApp {
  constructor(tracker) {
    this.tracker = tracker;
  }

  startTrackingWeather(city) {
    this.tracker.getWeather(city).then((weatherData) => {
      console.log(`Current weather in ${city}:`);
      console.log(`Temperature: ${weatherData.main.temp} K`);
      console.log(`Condition: ${weatherData.weather[0].description}`);
      this.tracker.addWeatherEntry(city, weatherData.main.temp, weatherData.weather[0].description);
    }).catch((error) => {
      console.error(error);
    });
  }

  getWeatherHistory() {
    return this.tracker.getWeatherHistory();
  }
}

const tracker = new WeatherTracker();
const app = new WeatherApp(tracker);

app.startTrackingWeather('London');
// app.getWeatherHistory();

// Example usage with async/await
async function main() {
  const weatherData = await tracker.getWeather('New York');
  console.log(`Current weather in New York:`);
  console.log(`Temperature: ${weatherData.main.temp} K`);
  console.log(`Condition: ${weatherData.weather[0].description}`);
}

main();
