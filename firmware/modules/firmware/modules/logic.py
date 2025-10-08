from modules import sensors, actuators, display
from modules.config import TIMING

def wet_clean():
    display.draw("Rain: WET", "Wet Clean")
    actuators.led_on()
    actuators.beep(TIMING["beep_long_ms"])
    actuators.pump_on()
    actuators.servo_sweep_once()
    actuators.led_off()

def dry_clean():
    display.draw("IR: Dust", "Dry Clean")
    actuators.led_on()
    actuators.beep(TIMING["beep_short_ms"], times=2)
    actuators.servo_sweep_once()
    actuators.led_off()

def loop():
    if sensors.is_rain():
        wet_clean()
    elif sensors.is_dust():
        dry_clean()
    else:
        display.draw("Idle", f"Light {sensors.light_pct()}%")
