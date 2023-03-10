import gyroscopeAccelerometr as ga
import gps, time
from setup import button, ledState, ledOnOff, ledError, end


def main():
    while True:
        ledOnOff.value(1)

        if button.value() == 1:
            while True:
                ledState.value(1)
                ledOnOff.value(1)
                try:
                    ledError.value(0)
                    gps.collectGPSData(gps.gpsModule)
                    ga.collectGAData()
                except KeyboardInterrupt:
                    end()
                except Exception:
                    ledError.value(1)
                
                if button.value() == 1:
                    ledState.value(0)
                    break
        else:
            ledState.value(0)
        time.sleep(0.1)
                
if __name__ == "__main__":
    main()
