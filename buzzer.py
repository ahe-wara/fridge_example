from machine import Pin

class Buzzer:
       
    def __init__(self, pin):
        self.__pin = pin
        self.__buzzer = Pin(self.__pin, Pin.OUT)
               
    def alarm_on(self):
        self.__buzzer.value(1)
        
    def alarm_off(self):
        self.__buzzer.value(0)
        