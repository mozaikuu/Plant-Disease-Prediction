# # @blynk.on("connected")
# import blynklib
# import time
# import random

# # Mock sensor values
# def mock_DHT_read():
#     return random.randint(1, 38), random.randint(0, 300)

# # Mock constants
# DHT_SENSOR = 'DHT11'
# DHT_PIN = 4

# # Replace with your Blynk Auth Token
# BLYNK_AUTH_TOKEN = 'tsLaqpG3IwyHX9NYSXuClCLtCa0CLeIt'

# # Initialize Blynk
# blynk = blynklib.Blynk(BLYNK_AUTH_TOKEN)

# # Function to handle connection event
# def blynk_connected():
#     print("Hi, You have Connected to New Blynk2.0")
#     print(".......................................................")
#     print("................... By SME Dehradun ...................")
#     blynk.sync_virtual(0, 1)  # Ensure the virtual pins are synchronized

# # Function for collecting data from sensor & sending it to the server
# def myData():
#     plant_class, soil_moisture = mock_DHT_read()
#     if plant_class is not None and soil_moisture is not None:
#         print("plant_class={0} soil_moisture={1}".format(plant_class, soil_moisture))
#     else:
#         print("Sensor failure. Check wiring.")
        
#     blynk.virtual_write(0, plant_class)
#     blynk.virtual_write(1, soil_moisture)
#     print("Values sent to New Blynk Server!")

# # Main loop to call myData function every 2 seconds
# connected = False
# while True:
#     blynk.run()
#     if not connected and blynk.connected():
#         blynk_connected()
#         connected = True
#     myData()
#     time.sleep(1)

# 2nd try

import blynklib
import time

# Blynk Auth Token
BLYNK_AUTH = 'tsLaqpG3IwyHX9NYSXuClCLtCa0CLeIt'

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Define a handler for virtual pin V0 write event
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    print(f"V1 value is: {value[2]}")

# Function to write value to V0
def write_to_virtual_pin(value):
    blynk.virtual_write(2, value)
    print(f"Wrote value {value} to V1")

# Run Blynk (this call should be non-blocking)
def main():
    while True:
        blynk.run()
        # Write a value to V0 every 5 seconds
        write_to_virtual_pin(1)
        time.sleep(5)
        write_to_virtual_pin(7)
        time.sleep(5)
        write_to_virtual_pin(38)
        time.sleep(5)
        write_to_virtual_pin(50)
        time.sleep(5)

if __name__ == '__main__':
    main()

# 3rd try

# from machine import Pin, I2C
# import network
# import time

# from blynklib import Blynk

# import constants


# i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
# BLYNK = Blynk(constants.BLYNK_AUTH_TOKEN)


# def connect_to_internet(ssid, password):
#     # Pass in string arguments for ssid and password

#     # Just making our internet connection
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(ssid, password)

#     # Wait for connect or fail
#     max_wait = 10
#     while max_wait > 0:
#         if wlan.status() < 0 or wlan.status() >= 3:
#             break
#         max_wait -= 1
#         print('waiting for connection...')
#         time.sleep(1)
#     # Handle connection error
#     if wlan.status() != 3:
#         print(wlan.status())
#         raise RuntimeError('network connection failed')
#     else:
#         print('connected')
#         print(wlan.status())
#         status = wlan.ifconfig()


# connect_to_internet(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)


# while True:
#     # bme = bme280.BME280(i2c=i2c)
#     # temperature, pressure, humidity = bme.read_compensated_data()
#     # Print sensor data to console
#     # print('Temperature: {:.1f} C'.format(temperature/100))
#     # print('Humidity: {:.1f} %'.format(humidity/1024))
#     # print('Pressure: {:.1f} hPa'.format(pressure/25600))
#     BLYNK.virtual_write(0, 17)
#     BLYNK.virtual_write(1, 123)
#     # BLYNK.virtual_write(9, pressure/25600)
#     BLYNK.run()
#     time.sleep(1)