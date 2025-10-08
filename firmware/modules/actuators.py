from machine import Pin, PWM
from time import sleep
from modules.config import PINS, TIMING

relay = Pin(PINS["RELAY1"], Pin.OUT)
buzzer = Pin(PINS["BUZZER"], Pin.OUT)
led = Pin(PINS["LED"], Pin.OUT)

servo = PWM(Pin(PINS["SERVO"])); servo.freq(50)

def pump_on(sec=TIMING["pump_on_s"]):
    relay.on(); sleep(sec); relay.off()

def beep(ms, times=1, gap=100):
    for _ in range(times):
        buzzer.on(); sleep(ms/1000); buzzer.off(); sleep(gap/1000)

def led_on(): led.on()
def led_off(): led.off()

def servo_sweep_once():
    for a in range(0,181,10): _servo_angle(a); sleep(0.02)
    for a in range(180,-1,-10): _servo_angle(a); sleep(0.02)

def _servo_angle(deg):
    us = 500 + int((2000*deg)/180)   # 0.5ms..2.5ms
    duty = int(us*65535/20000)
    servo.duty_u16(duty)
