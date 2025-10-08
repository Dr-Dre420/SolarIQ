from machine import Pin, I2C
import ssd1306
from modules.config import PINS

i2c = I2C(0, scl=Pin(PINS["OLED_SCL"]), sda=Pin(PINS["OLED_SDA"]), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw(msg, sub=""):
    oled.fill(0)
    oled.text("Solar IQ", 0, 0)
    oled.text(msg, 0, 16)
    if sub: oled.text(sub, 0, 32)
    oled.show()
