# CobraSoftware

![Czech][czechLangBadge]
![Lines of code][codeLinesBadge]

Cobra software for rockets with RaspberryPi Pico control centre in Micropython

## Quick startguide

- If you don't have any previous experience with RaspberryPi Pico, you can start with [this tutorial][pico-GetStarted] to quickly get started with it.
- [Tutorial about connecting RaspberryPi Pico with MPU6050][MPU6050Link]
- [Tutorial about connecting RaspberryPi Pico with GPS module][GPSLink]

### Wiring MPU6050

![MPU6050 wiring][MPU6050Image]
Connect the circuit exactly as shown on the image below, you can simply change pins in the **setup.py** file.
You have to download this external files **imu.py**, **vector3d.py** from [github][MPUEXTERNALFILES]
:warning: It may take a few tens of seconds for the output to stabilize.

- [Nice tutorial about connecting MPU6050 with RaspberryPi Pico on peppe8o.com][MPU6050Link]

### Wiring GPS Neo-6M

![GPS wiring][GPSImage]
Connect GND to GND, 3v3(OUT) to VCC, GP4 to RX and GP5 to TX, you can simply change pins in the **setup.py** file.
:warning: GPS module should be ideally outside to work correctly. Otherwise it will just print no data.

- [Article about GPS module with RaspberryPi Pico on microcontrollerslab.com][GPSLink]

### Wiring Buttons and LEDs

Connect **first LED** to the **GP9** and GND, and **second LED** to the **GP12** and GND, don't forget about resistors.
**Button** is connected defaultly on the **GP7** and connected to GND obviously. After pressing button first LED should light on, and pico should start writing data to the files (printing to the console in [thonny](https://thonny.org)). If something fails, second LED should brighten up.

### Analyzing data

#### Requirements

```python
pip install matplotlib
```

After collecting data to the files download them to the same directory as **graph.py** and run it in terminal ```python3 graph.py``` It will create some graphs and you can view your data from gyroscope and accelerometer. Before new measurments you have to delete previous data from .csv files. **Right now there is not our program for analyzing GPS coordinates, but in the future updates we will add many other modules**

## Bugs / Features

Known problems:

- Time is reseted while not connected to PC or GPS satellite to the 2021/1/1
- GPS module is weak and often doesn't establish connection with satellites

[czechLangBadge]: https://img.shields.io/badge/MADE%20IN-CZECH-red?style=for-the-badge
[codeLinesBadge]: https://img.shields.io/tokei/lines/github/foglar/Cobra-Project?color=green&style=for-the-badge

[pico-GetStarted]: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico

[MPUEXTERNALFILES]: https://github.com/micropython-IMU/micropython-mpu9x50
[MPU6050Image]: https://raw.githubusercontent.com/foglar/Cobra-Project/main/Raspberry-PI-Pico-MPU6050.webp
[MPU6050Link]: https://peppe8o.com/using-gyroscope-and-accelerometer-with-mpu6050-raspberry-pi-pico-and-micropython/

[GPSImage]: https://raw.githubusercontent.com/foglar/Cobra-Project/main/Raspberry-Pi-Pico-NEO6M.jpg
[GPSLink]: https://microcontrollerslab.com/neo-6m-gps-module-raspberry-pi-pico-micropython/
