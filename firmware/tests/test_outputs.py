from firmware.modules import actuators, display

def test_actuators():
    display.draw("Testing...", "")
    actuators.led_on()
    actuators.beep(200, times=2)
    actuators.led_off()
    actuators.pump_on(1)
    actuators.servo_sweep_once()

if __name__ == "__main__":
    test_actuators()
