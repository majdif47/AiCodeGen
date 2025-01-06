import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta

# Function to scrape movie schedules from the website of an Indian theater chain
def get_movie_schedules(theater_name, showtime):
    url = f"https://www.{theater_name}.com/movie/{showtime}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract showtime data from HTML
            for movie in soup.find_all('div', class_='movie-data'):
                start_time = movie.find('div', class_='show-time').text.strip()
                end_time = movie.find('div', class_='end-time').text.strip()
                
                print(f"Movie: {start_time} - {end_time}")
        else:
            print("Failed to retrieve data:", response.status_code)
    except Exception as e:
        print(e)

# Usage example
theater_name = "pvr"
showtime = "morning show"

get_movie_schedules(theater_name, showtime)
