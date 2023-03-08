import gyroscopeAccelerometr as ga
import gps
from setup import button, ledState, ledOnOff, ledError

def main():
    while True:
        
        ledOnOff.value(1)
        if button.value() == 0:
            ledState.value(1)
            try:
                gps.collectGPSData(gps.gpsModule)
                ga.collectGAData()
            except:
                ledError.value(1)
        else:
            ledState.value(0)
    

if __name__ == "__main__":
    main()
