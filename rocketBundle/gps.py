from machine import Pin, UART, I2C
from setup import timeNow, gpsTXPin as tx, gpsRXPin as rx

# Initialisation of GPS communication
gpsModule = UART(1, baudrate=9600, tx=tx, rx=rx)
buff = bytearray(255)

# Get output from Neo6M
def collectGPSData(gpsModule):
    data = []
    buff = str(gpsModule.readline())
    parts = buff.split(",")
    if parts[0][:2] == "b'":
        
        buff = buff.replace("b'", '')
        
        if parts[0] == "b'$GPGGA":
            print(buff)
            data.append(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        if parts[0] == "b'$GPRMC":
            print(buff)
            data.append(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        if parts[0] == "b'$GPGSA":
            print(buff)
            data.append(
                "%s, %s\n"
                % (timeNow(), buff)
            )
        if parts[0] == "b'$GPGSV":
            print(buff)
            data.append(
                "%s, %s\n"
                % (timeNow(), buff)
            )
    return data



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
        print(collectGPSData(gpsModule), end="\r")


if __name__ == "__main__":
    main()