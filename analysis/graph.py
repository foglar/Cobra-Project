#!/usr/bin/env python3

# Import external libraries
import matplotlib.pyplot as plt
import csv
import math
from pathlib import Path

# Main function
def main():
    # Read data from csv file
    data = read_csv(filename=Path("dataFile.csv"))
    # Convert time from csv file to a list of strings
    time = convertData(data, 0, "time")
    # Convert data from csv file to a list of floats
    dataX = convertData(data, 1, "num")
    dataY = convertData(data, 2, "num")
    dataZ = convertData(data, 3, "num")
    dataXA = convertData(data, 4, "num")
    dataYA = convertData(data, 5, "num")
    dataZA = convertData(data, 6, "num")
    temp = convertData(data, 7, "temp")

    # Average data from same time
    averageXValue = averageTime(time, dataX)
    gyroscopeX = radToDegrees(averageXValue)
    averageYValue = averageTime(time, dataY)
    gyroscopeY = radToDegrees(averageYValue)
    averageZValue = averageTime(time, dataZ)
    gyroscopeZ = radToDegrees(averageZValue)

    averageXAValue = averageTime(time, dataXA)
    averageYAValue = averageTime(time, dataYA)
    averageZAValue = averageTime(time, dataZA)
    averageTempValue = averageTime(time, temp)

    # Remove duplicates from time list
    time = removeDuplicates(time)
    # Create graphs
    graphs(
        gyroscopeX,
        gyroscopeY,
        gyroscopeZ,
        averageXAValue,
        averageYAValue,
        averageZAValue,
        averageTempValue,
        time,
    )


# Read data from csv file
def read_csv(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# Convert data from csv file to a list of floats
def convertData(data, index, dataType):
    dataOut = [0] * len(data)
    if dataType == "num":
        for i in range(len(data)):
            dataOut[i] = round(float(data[i][index]), 2)
    elif dataType == "time":
        for i in range(len(data)):
            dataOut[i] = data[i][index]
    elif dataType == "temp":
        for i in range(len(data)):
            dataOut[i] = round(float(data[i][index]))
    else:
        print("Invalid dataType")
    return dataOut


# Average data from same time
def averageTime(time, data):
    LIST_OF_VALUES_FROM_SAME_TIME = []
    averageValue = []
    for i in range(len(time)):  # Loop through time list
        if (
            time[i] == time[i - 1]
        ):  # If time is the same as previous time add time to list
            LIST_OF_VALUES_FROM_SAME_TIME.append(data[i])
        else:  # If time is not the same as previous time average list and add to averageValue list
            try:
                averageValue.append(
                    sum(LIST_OF_VALUES_FROM_SAME_TIME)
                    / len(LIST_OF_VALUES_FROM_SAME_TIME)
                )
            except ZeroDivisionError:  # If error of ZERO division occurs
                pass
            LIST_OF_VALUES_FROM_SAME_TIME.clear()  # Clear list so it can be used again
    # return list of averaged values
    return averageValue


# Remove duplicates from time list
def removeDuplicates(list):
    new_list = []
    for a in list:  # Loop through list
        if a not in new_list:  # If value is not in new_list add to new_list
            new_list.append(a)
    return new_list


# Create graphs
def graphs(xg, yg, zg, xa, ya, za, temp, time):
    # Create graph of gyroscope and accelerometre data together
    fig1, (ax1, ax2) = plt.subplots(2, 1)
    fig1.suptitle("Gyroscope and Accelerometre Data")
    # Gyroscope
    ax1.plot(xg, label="X")
    ax1.plot(yg, label="Y")
    ax1.plot(zg, label="Z")
    ax1.legend("XYZ")
    ax1.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    # Accelerometre
    ax2.plot(xa, label="X")
    ax2.plot(ya, label="Y")
    ax2.plot(za, label="Z")
    ax2.legend("XYZ")
    ax2.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))

    # Create graph of temperature
    fig2, ax3 = plt.subplots()
    fig2.suptitle("Temperature")
    ax3.plot(temp, label="Temperature")

    # Create graph of gyroscope and accelerometre data separated
    # Gyroscope
    fig3, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig3.suptitle("Gyroscope Data Separated")
    # GyroscopeX
    ax1.plot(xg, label="X")
    ax1.legend("X")
    ax1.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax1.set_ylabel("x - angle")
    # GyroscopeY
    ax2.plot(yg, label="Y", color="orange")
    ax2.legend("Y")
    ax2.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax2.set_ylabel("y - angle")
    # GyroscopeZ
    ax3.plot(zg, label="Z", color="green")
    ax3.legend("Z")
    ax3.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax3.set_ylabel("z - angle")

    # Accelerometre
    fig4, (ax4, ax5, ax6) = plt.subplots(3, 1)
    fig4.suptitle("Accelerometre Data Seaprated")
    # AccelerometreX
    ax4.plot(xa, label="X")
    ax4.legend("X")
    ax4.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax4.set_ylabel("x - angle")
    # AccelerometreY
    ax5.plot(ya, label="Y", color="orange")
    ax5.legend("Y")
    ax5.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax5.set_ylabel("y - angle")
    # AccelerometreZ
    ax6.plot(za, label="Z", color="green")
    ax6.legend("Z")
    ax6.set_xlabel("time [s] %s - %s" % (time[0], time[-1]))
    ax6.set_ylabel("z - angle")

    plt.show()


def radToDegrees(data):
    for i in range(len(data)):
        data[i] = round(data[i] * 180 / math.pi, 3)
    return data


# Run program as main
if __name__ == "__main__":
    main()
