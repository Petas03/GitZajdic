import network
import socket
import time
import machine
import json

SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print('Connecting to network...')
    time.sleep(1)

print('Network connected:', wlan.ifconfig())

# Initialize socket
addr = socket.getaddrinfo('api.weatherapi.com', 80)[0]

s = socket.socket()
print('Socket created')

# Function to get weather data
def get_weather(location):
    url = f'/v1/current.json?key=YOUR_API_KEY&q={location}'
    s.connect(addr)
    s.send('GET ' + url + ' HTTP/1.0\r\nHost: api.weatherapi.com\r\n\r\n')
    response = s.recv(1024)
    s.close()
    return response

location = 'London'
weather_data = get_weather(location)
print('Weather Data:', weather_data)