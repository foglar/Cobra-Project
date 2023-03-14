from machine import Pin, UART, I2C
from setup import timeNow, gpsTXPin as tx, gpsRXPin as rx
import time

# Initialisation of GPS communication
gpsModule = UART(1, baudrate=9600, tx=tx, rx=rx)
buff = bytearray(255)

# Get output from Neo6M
def collectGPSData(gpsModule):

    buff = str(gpsModule.readline())
    parts = buff.split(",")
    dataFile = open("dataFileGPS.csv", "a")
    if parts[0][:2] == "b'":
        
        buff = buff.replace("b'", '')
        
        if parts[0] == "b'$GPGGA":
            print(buff)
            dataFile.write(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        elif parts[0] == "b'$GPRMC":
            print(buff)
            dataFile.write(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        elif parts[0] == "b'$GPGSA":
            print(buff)
            dataFile.write(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        elif parts[0] == "b'$GPGSV":
            print(buff)
            dataFile.write(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        else:
            print("No GPS data", end="\n")

    dataFile.close()


# Convert values to degrees
def convertToDegree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat / 100)
    nexttwodigits = RawAsFloat - float(firstdigits * 100)

    Converted = float(firstdigits + nexttwodigits / 60.0)
    Converted = "{0:.6f}".format(Converted)
    return str(Converted)


# Main loop
def main():
    while True:

        collectGPSData(gpsModule)


if __name__ == "__main__":
    main()