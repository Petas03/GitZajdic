import requests
import time

API_KEY = 'your_api_key'  # Replace with your actual API key
CITY = 'your_city'         # Replace with the city for which you want the weather
API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

def fetch_weather():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        display_weather(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def display_weather(data):
    # Example display format
    print(f"Weather in {data['name']}:\n")
    print(f"Temperature: {data['main']['temp']}K\n")
    print(f"Weather: {data['weather'][0]['description']}\n")

def main():
    while True:
        fetch_weather()
        print("Waiting for the next update...")
        time.sleep(600)  # Sleep for 10 minutes

if __name__ == "__main__":
    main()