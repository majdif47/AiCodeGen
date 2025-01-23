class WeatherStation {
  constructor() {
    this.temperature = null;
    this.humidity = null;
    this.pressure = null;
    this.lastUpdated = new Date();
  }

  updateValues(temp, humid, press) {
    this.temperature = temp;
    this.humidity = humid;
    this.pressure = press;
    this.lastUpdated = new Date();
  }

  getStationData() {
    const now = new Date();
    if (now.getTime() - this.lastUpdated.getTime() > 300000) { // 5 minutes
      return null;
    }
    return `${this.temperature}°C, ${this.humidity}% RH, ${this.pressure} mbar`;
  }
}

class WeatherLogger {
  constructor(station) {
    this.station = station;
    this.logFile = 'weatherlog.txt';
  }

  logCurrentData() {
    const data = this.station.getStationData();
    if (data !== null) {
      const timestamp = new Date().toLocaleString();
      const logLine = `${timestamp} - ${data}\n`;
      fs.appendFileSync(this.logFile, logLine);
    }
  }

  startLogging() {
    setInterval(() => {
      this.logCurrentData();
    }, 300000); // every 5 minutes
  }
}

// Example usage:
const station = new WeatherStation();
const logger = new WeatherLogger(station);
logger.startLogging();

