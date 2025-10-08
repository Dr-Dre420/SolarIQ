from machine import Pin, ADC
from time import sleep_us
from modules.config import PINS

rain = Pin(PINS["RAIN"], Pin.IN)
ir   = Pin(PINS["IR"],   Pin.IN)
ldr  = ADC(PINS["LDR_ADC"])

def is_rain(): return rain.value() == 0
def is_dust(): return ir.value() == 0
def light_pct(): return int(ldr.read_u16() * 100 / 65535)
