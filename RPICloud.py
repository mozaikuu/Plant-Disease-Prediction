import blynklib
import Adafruit_DHT
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
BLYNK_AUTH_TOKEN = 'tsLaqpG3IwyHX9NYSXuClCLtCa0CLeIt'

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH_TOKEN)

# Create BlynkTimer Instance
timer = BlynkTimer()


# function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Hi, You have Connected to New Blynk2.0")
    print(".......................................................")
    print("................... By SME Dehradun ...................")
    time.sleep(2);

# Functon for collect data from sensor & send it to Server
def myData(plant_class, soil_moisture):
    if plant_class is not None and soil_moisture is not None:
        print("plant_class={0:0.1f}C soil_moisture={1:0.1f}%".format(plant_class, soil_moisture))
    else:
        print("Sensor failure. Check wiring.");

    blynk.virtual_write(0, plant_class,)
    blynk.virtual_write(1, soil_moisture)
    print("Values sent to New Blynk Server!")

# timer.set_interval(2, myData)