# import time
# import RPi.GPIO as GPIO
# import requests
# import json

# # Function to read soil moisture
# def soil_moisture_sensor():
#     # Code to read soil moisture sensor
#     # ...
#     # Return the soil moisture value
#     return soil_moisture_value

# # Function to detect plant disease
# def Plant_disease_detection():
#     # Code to detect plant disease
#     # ...
#     # Return the disease status
#     return disease_status

# def send_data(data):
#     try:
#         response = requests.post(url, json=data)
#         response.raise_for_status()
#         print("Data sent successfully!")
#     except requests.exceptions.RequestException as e:
#         print("Error sending data:", str(e))

# def Cloud():
#     while True:
#         # Read soil moisture
#         soil_moisture = soil_moisture_sensor()

#         # Detect plant disease
#         disease = Plant_disease_detection()

#         # Prepare data
#         data = {
#             "soil_moisture": soil_moisture,
#             "disease": disease
#         }

#         # Send data to server
#         send_data(data)

#         # Sleep for 10 seconds
#         time.sleep(10)

# if __name__ == "__main__":
#     main()