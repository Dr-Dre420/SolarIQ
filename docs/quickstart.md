# Solar IQ Quickstart

## Flashing Pico
1. Install MicroPython firmware via Thonny.
2. Set interpreter to `MicroPython (Raspberry Pi Pico)`.

## Wiring summary
- OLED: SDA → GP0, SCL → GP1
- Rain sensor → GP14
- IR sensor → GP15
- Relay IN1 → GP17
- Buzzer → GP19
- LED → GP22 (with 220Ω)
- Servo → GP2
- LDR → GP26 (divider)
- DHT11 → GP16

## Running demo
- Copy all modules + main.py to Pico.
- On boot, it shows “System Ready”.
- Trigger rain or IR, see actions happen.

## Troubleshooting
- No OLED text → check I2C address or wiring
- DHT fails readings → wait 2s between measure calls
- Unexpected resets → add 1000 µF capacitor on 5V rail.
