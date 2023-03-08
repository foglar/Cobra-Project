from machine import Pin, UART, I2C
from setup import timeNow, gpsTXPin as tx, gpsRXPin as rx

# Initialisation of GPS communication
gpsModule = UART(1, baudrate=9600, tx=tx, rx=rx)
buff = bytearray(255)

# Setting default variables
FIX_STATUS = False

latitude = ""
longitude = ""
satellites = ""
GPStime = ""

# Get output from Neo6M
def collectGPSData(gpsModule):
    global FIX_STATUS, latitude, longitude, satellites, GPStime

    gpsModule.readline()
    buff = str(gpsModule.readline())
    parts = buff.split(",")
    dataFile = open("dataFileGPS.csv", "a")
    if parts[0] == "b'$GPGGA" and len(parts) == 15:
        if (
            parts[1]
            and parts[2]
            and parts[3]
            and parts[4]
            and parts[5]
            and parts[6]
            and parts[7]
        ):
            print(buff)

            latitude = convertToDegree(parts[2])
            if parts[3] == "S":
                latitude = -latitude
            longitude = convertToDegree(parts[4])
            if parts[5] == "W":
                longitude = -longitude
            satellites = parts[7]
            GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
            FIX_STATUS = True
            print(
                "Latitude: %s  Longitude: %s  Satellites: %s  Time: %s"
                % (latitude, longitude, satellites, GPStime),
                end="\n",
            )
            dataFile.write(
                "%s, %s, %s, %s, %s\n"
                % (timeNow(), latitude, longitude, satellites, GPStime)
            )
    else:
        print("No GPS data", end="\n")
        dataFile.write("%s NODATA\n" % (timeNow()))

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
    global FIX_STATUS
    while True:

        collectGPSData(gpsModule)

        if FIX_STATUS == True:
            print("Printing GPS data...")
            print(" ")
            print("Latitude: " + latitude)
            print("Longitude: " + longitude)
            print("Satellites: " + satellites)
            print("Time: " + GPStime)
            print("----------------------")

            FIX_STATUS = False


if __name__ == "__main__":
    main()
