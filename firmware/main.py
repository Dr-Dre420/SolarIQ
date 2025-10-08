from time import sleep
from modules import logic, display

display.draw("System Ready")
while True:
    logic.loop()
    sleep(0.5)
