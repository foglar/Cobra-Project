from machine import Pin, I2C
from time import sleep
import bme280  # importing BME280 library
from setup import timeNow, tempSDAPin as sda, tempSCLPin as scl

i2c = I2C(0, sda=sda, scl=scl, freq=400000)  # initializing the I2C method


def collectTempData():
    dataFile = open("dataFileBME.csv", "a")
    bme = bme280.BME280(i2c=i2c)
    temperature = bme.values[0]  # reading the value of temperature
    pressure = bme.values[1]  # reading the value of pressure
    humidity = bme.values[2]  # reading the value of humidity
    dataFile.write("%s, %s\n" % (timeNow(), temperature, pressure, humidity))
    dataFile.close()
    return temperature, pressure, humidity


def main():
    while True:
        print(
            "Temperature: ",
            collectTempData()[0],
            "Pressure: ",
            collectTempData()[1],
            "Humidity: ",
            collectTempData()[2],
        )
        sleep(1)


if __name__ == "__main__":
    main()
