import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

result = instance.read()

print("===" + str(datetime.datetime.now())+"===")
time.sleep(1)
print(vars(result))