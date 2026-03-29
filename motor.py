from machine import Pin

# ======== 1. 硬件引脚配置 ========
# 左轮: GP0 / GP1
# 右轮: GP2 / GP3
left_in1 = Pin(0, Pin.OUT)
left_in2 = Pin(1, Pin.OUT)
right_in3 = Pin(2, Pin.OUT)
right_in4 = Pin(3, Pin.OUT)

# ======== 2. 基础动作封装 ========
def stop():
    """停车：所有控制引脚拉低。"""
    left_in1.value(0)
    left_in2.value(0)
    right_in3.value(0)
    right_in4.value(0)


def forward():
    """前进：左右轮都向前转。"""
    left_in1.value(1)
    left_in2.value(0)
    right_in3.value(1)
    right_in4.value(0)


def backward():
    """后退：左右轮都向后转。"""
    left_in1.value(0)
    left_in2.value(1)
    right_in3.value(0)
    right_in4.value(1)


def turn_left():
    """左转：左轮后退，右轮前进。"""
    left_in1.value(0)
    left_in2.value(1)
    right_in3.value(1)
    right_in4.value(0)


def turn_right():
    """右转：左轮前进，右轮后退。"""
    left_in1.value(1)
    left_in2.value(0)
    right_in3.value(0)
    right_in4.value(1)

# 文件被导入时，先确保小车处于停止状态。
stop()