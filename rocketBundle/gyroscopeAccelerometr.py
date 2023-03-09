from imu import MPU6050
from machine import Pin, I2C
from setup import timeNow, gyroscopeSDAPin as pinSDA, gyroscopeSCLPin as pinSCL, end

# Initialisation of MPU6050 communication
i2c = I2C(0, sda=Pin(pinSDA), scl=Pin(pinSCL), freq=400000)
imu = MPU6050(i2c)

# Get output from MPU6050
def collectGAData():
    try:
        # Open csv table for input
        dataFile = open("dataFile.csv", "a")

        # Save output to variables
        ax = round(imu.accel.x, 2)
        ay = round(imu.accel.y, 2)
        az = round(imu.accel.z, 2)
        gx = imu.gyro.x
        gy = imu.gyro.y
        gz = imu.gyro.z
        tem = round(imu.temperature, 2)

        # Print output and write output to table
        print(
            "TIME: %s | aX: %s  aY: %s  aZ: %s  gX: %s  gY: %s  gZ: %s  Temperature: %s     \n"
            % (timeNow(), ax, ay, az, gx, gy, gz, tem)
        )
        dataFile.write(
            "%s, %s, %s, %s, %s, %s, %s, %s\n"
            % (timeNow(), ax, ay, az, gx, gy, gz, tem)
        )

        # Delay and Close File
        dataFile.close()

    # Check for keyboard interrupt
    except KeyboardInterrupt:
        end()


# Main loop
def main():
    while True:
        collectGAData()


if __name__ == "__main__":
    main()
