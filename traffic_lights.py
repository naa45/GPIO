from gpiozero import LED
from time import sleep

red = LED(27)
amber = LED(17)
green = LED(22)

red.blink(1, 1)
amber.blink(2, 2)
green.blink(3, 3)

while True:
    red.toggle()
    sleep(1)
    amber.toggle()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    sleep(0)
    amber.off()
    sleep(0)
    green.off()
