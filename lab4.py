import math
import time
from machine import Pin, PWM


f = 0.2
T = 1/f
phi = math.pi/7

ps = Pin(7, Pin.IN, Pin.PULL_DOWN)

debounce_ms = 50

def reverse(ps):
    print(f' Transition detected on {ps}, value = {ps.value()}')
    global phi
    phi = -phi
    
def debounced(callback, delay_ms=debounce_ms):
    last = [0]
    def handler(ps):
        now = time.ticks_ms()
        if time.ticks_diff(now, last[0]) > delay_ms:
            last[0] = now
            callback(ps)
    return handler
    

    
ps.irq(handler=debounced(reverse), trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

try: 
    while True:
        t = time.ticks_ms()/1000
          
            
        pwm0 = PWM(Pin(0), freq = 500, duty = int((100*(math.sin(2*math.pi*f*t))**2)))
            
        pwm1 = PWM(Pin(1), freq = 500, duty = int(100*(math.sin(2*math.pi*f*t - phi))**2))
            
        pwm2 = PWM(Pin(3), freq = 500, duty = int(100*(math.sin(2*math.pi*f*t - 2*phi))**2))
            
        pwm3 = PWM(Pin(21), freq = 500, duty = int(100*(math.sin(2*math.pi*f*t - 3*phi))**2))
    
        pwm4 = PWM(Pin(5), freq = 500, duty = int(100*(math.sin(2*math.pi*f*t - 4*phi))**2))
        
        pwm5 = PWM(Pin(6), freq = 500, duty = int(100*(math.sin(2*math.pi*f*t - 5*phi))**2))
   
   
except KeyboardInterrupt:
    pwm.deinit()
    