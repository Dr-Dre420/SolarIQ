from firmware.modules import sensors

def test_rain_ir():
    print("Rain sensor:", "Wet" if sensors.is_rain() else "Dry")
    print("IR sensor:", "Dust" if sensors.is_dust() else "Clear")

def test_light():
    print("Light %:", sensors.read_light_pct())

if __name__ == "__main__":
    test_rain_ir()
    test_light()
