import time
from fridge_switch import FridgeSwitch
from buzzer import Buzzer

fridge_switch = FridgeSwitch(16, False)
buzzer = Buzzer(15)
fridge_State = False

while True:
    if fridge_switch.get_alarm():
        buzzer.alarm_on()
    elif not fridge_switch.get_alarm():
        buzzer.alarm_off()
    time.sleep_ms(100)

