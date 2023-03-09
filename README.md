# CobraSoftware

![Czech][czechLangBadge]
![Lines of code][codeLinesBadge]
![GitHub issues](https://img.shields.io/github/issues/foglar/Cobra-Project?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/foglar/Cobra-Project?style=for-the-badge)

Cobra software for rockets with RaspberryPi Pico control centre in Micropython

[![CodeFactor](https://www.codefactor.io/repository/github/foglar/cobra-project/badge)](https://www.codefactor.io/repository/github/foglar/cobra-project)
![GitHub top language](https://img.shields.io/github/languages/top/foglar/Cobra-Project)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/foglar/Cobra-Project)
![GitHub Repo stars](https://img.shields.io/github/stars/foglar/Cobra-Project?style=social)

## Quick startguide

### Preparation

- Download Thonny IDE from [here][thonnyLink]
- We are using [RaspberryPi Pico][raspberryPiPico] and [Micropython][micropython], so you have to download UF2 bootloader for [RaspberryPi Pico][micropythonLink] or [RaspberryPi Pico W][micropythonLinkW]
- We use **[MPU6050][MPU6050Link]** and **[GPS Neo-6M][GPSLink]** modules with **TP4056 USB-C Li-Pol bateries charger** and **Li-Pol battery**. But you can adapt the code for your hardware modules. You also need 2 **leds** and one **button**
- For using our graphing program you have to install **matplotlib** library ```pip3 install matplotlib```

### Learn more about it

- If you don't have any previous experience with RaspberryPi Pico, you can start with [this tutorial][pico-GetStarted] to quickly get started with it.
- [Tutorial about connecting RaspberryPi Pico with MPU6050][MPU6050Link]
- [Tutorial about connecting RaspberryPi Pico with GPS module][GPSLink]

![pinout][pinout]

### Wiring MPU6050

Connect the circuit exactly as shown on the image below, you can simply change pins in the **setup.py** file.
You have to download this external files **imu.py**, **vector3d.py** from [github][MPUEXTERNALFILES]
:warning: It may take a few tens of seconds for the output to stabilize.

- [Nice tutorial about connecting MPU6050 with RaspberryPi Pico on peppe8o.com][MPU6050Link]

### Wiring GPS Neo-6M

Connect GND to GND, 3v3(OUT) to VCC, GP4 to RX and GP5 to TX, you can simply change pins in the **setup.py** file.
:warning: GPS module should be ideally outside to work correctly. Otherwise it will just print no data.

- [Article about GPS module with RaspberryPi Pico on microcontrollerslab.com][GPSLink]

### Wiring Buttons and LEDs

Connect **first LED** to the **GP9** and GND, and **second LED** to the **GP12** and GND, don't forget about resistors.
**Button** is connected defaultly on the **GP7** and connected to GND obviously. After pressing button first LED should light on, and pico should start writing data to the files (printing to the console in [thonny][thonnyLink]). If something fails, second LED should brighten up.

### Setting up

- After connection of all modules, you have to set up the **setup.py** file. You have to set up the **GPS** and **MPU6050** pins, and also set up the **LEDs** and **button** pins. If you setup your modules as instructions says, you can skip this step.
- If everything works, you can power your [pico][raspberryPiPico] with battery, connected to the **TP4056 USB-C Li-Pol bateries charger** to the any **GND** and **VSYS**, so you can use it without PC. If you want to use it with PC, you have to connect it via USB-C cable to the PC and power it via USB-C cable. Run your scripts by pressing the button, and stop by pressing button again. First led will be on, if your script is running. Second led indicates serious error in code.

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

[raspberryPiPico]: https://www.raspberrypi.com/products/raspberry-pi-pico/

[thonnyLink]: https://thonny.org
[micropython]: https://micropython.org/
[micropythonLink]: https://micropython.org/download/rp2-pico/
[micropythonLinkW]: https://micropython.org/download/rp2-pico-w/

[pico-GetStarted]: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico

[pinout]: https://raw.githubusercontent.com/foglar/Cobra-Project/main/pinout.png

[MPUEXTERNALFILES]: https://github.com/micropython-IMU/micropython-mpu9x50
[MPU6050Link]: https://peppe8o.com/using-gyroscope-and-accelerometer-with-mpu6050-raspberry-pi-pico-and-micropython/

[GPSLink]: https://microcontrollerslab.com/neo-6m-gps-module-raspberry-pi-pico-micropython/
