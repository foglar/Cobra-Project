import time
from machine import Pin

# Pins setup
buttonPin = 7  # Button to start data collection
ledStatePin = 11  # LED to show if scanning is working
ledErrorPin = 12  # LED to show if there is an error
# Gyroscope and Accelerometer
gyroscopeSDAPin, gyroscopeSCLPin = 0, 1  # Set your own values
# GPS
gpsTXPin, gpsRXPin = 4, 5  # Set your own values
ledOnOff = Pin('LED', Pin.OUT)  # LED on or off

# External connections initialisation
button = Pin(buttonPin, Pin.IN, Pin.PULL_UP)
ledState = Pin(ledStatePin, Pin.OUT)
ledError = Pin(ledErrorPin, Pin.OUT)
gpsRXPin = Pin(gpsRXPin)
gpsTXPin = Pin(gpsTXPin)

# Get current time
def timeNow():
    currentTime = time.localtime()
    ctime = "%s/%s/%s %s:%s:%s" % (
        currentTime[0],
        currentTime[1],
        currentTime[2],
        currentTime[3],
        currentTime[4],
        currentTime[5],
    )
    return ctime