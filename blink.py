from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED 示例开始")
print("板载 LED 会闪烁 5 次")

for _ in range(5):
    pin.toggle()
    sleep(0.5)
    pin.toggle()
    sleep(0.5)

pin.off()
print("LED 示例结束")
