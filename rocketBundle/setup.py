import time, sys, gps, gyroscopeAccelerometr as ga, temperature as temp
from machine import Pin

# Pins setup
buttonPin = 7  # Button to start data collection
ledStatePin = 11  # LED to show if scanning is working
ledErrorPin = 12  # LED to show if there is an error
# Gyroscope and Accelerometer
gyroscopeSDAPin, gyroscopeSCLPin = 0, 1  # Set your own values
# GPS
gpsTXPin, gpsRXPin = 4, 5  # Set your own values
ledOnOff = Pin("LED", Pin.OUT)  # LED on or off
# Temperature and Humidity
tempSDAPin, tempSCLPin = 16, 17  # Set your own values


# External connections initialisation
button = Pin(buttonPin, Pin.IN, Pin.PULL_UP)
ledState = Pin(ledStatePin, Pin.OUT)
ledError = Pin(ledErrorPin, Pin.OUT)
gpsRXPin = Pin(gpsRXPin)
gpsTXPin = Pin(gpsTXPin)
tempSCLPin = Pin(tempSCLPin)
tempSDAPin = Pin(tempSDAPin)

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


def end():
    print("Keyboard interrupt detected. Exiting...")
    for i in range(3):
        ledOnOff.value(0)
        ledState.value(0)
        ledError.value(0)
        time.sleep(1)
        ledOnOff.value(1)
        ledState.value(1)
        ledError.value(1)
        time.sleep(1)
    sys.exit()

def saveData():
    f = open("data.csv", "a")
    gps_data = gps.collectGPSData(gps.gpsModule)
    gyro_accelero = ga.collectGAData()
    temperature = temp.collectTempData()
    f.write(
        f"{timeNow()}, {gps_data}, {gyro_accelero}, {temperature}\n"
    )
