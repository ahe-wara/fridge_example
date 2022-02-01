from machine import Pin
from machine import Timer
import time

class FridgeSwitch:
       
    def __init__(self, pin, alarm):
        self.__pin = pin
        self.__switch = Pin(self.__pin, Pin.IN, Pin.PULL_UP)
        self.__alarm = alarm
        self.__switch.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.__button_handler)
        self.__timer = Timer()
        #initial switch check
        self.__button_handler(self.__switch)

    def __button_handler(self, Pin):
        time.sleep_ms(50)
        if self.__switch.value():
           #print(self)
           #print(Pin)
           self.__start_alarm()
        elif not self.__switch.value():
           #print(self)
           #print(Pin.value())
           self.__stop_alarm()
    
    def __start_alarm(self):
            self.__timer.init(mode=Timer.ONE_SHOT, period=10000, callback=self.__timer_handler)
              
    def __timer_handler(self, t):
        #print(self)
        #print(t)
        self.__alarm = True
    
    def __stop_alarm(self):
        #print("alarm stopped")
        self.__alarm = False
        self.__timer.deinit()
           
    def get_alarm(self):
        #print(self.__alarm)
        return self.__alarm