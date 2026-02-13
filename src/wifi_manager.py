# wifi_manager.py

# This script provides Wi-Fi connection management for Raspberry Pi Pico W.

import network
import time

class WiFiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wifi = network.WLAN(network.STA_IF)

    def connect(self):
        self.wifi.active(True)
        self.wifi.connect(self.ssid, self.password)
        print('Connecting to network...')

        # Wait for connection
        timeout = 10
        start_time = time.time()
        while not self.wifi.isconnected():
            if time.time() - start_time > timeout:
                print('Connection failed!')
                return False
            time.sleep(1)

        print('Connected to Wi-Fi:', self.wifi.ifconfig())
        return True

    def disconnect(self):
        if self.wifi.isconnected():
            self.wifi.disconnect()
            print('Disconnected from Wi-Fi')
        else:
            print('Already disconnected')