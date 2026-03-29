from machine import Pin

# ======== 1. 硬件引脚配置 ========
# 左轮: GP0 / GP1
# 右轮: GP2 / GP3
LEFT_IN1_PIN = 2
LEFT_IN2_PIN = 3
RIGHT_IN3_PIN = 0
RIGHT_IN4_PIN = 1

# 某一侧电机如果前进/后退方向反了，只改这里，不用改动作函数。
LEFT_MOTOR_REVERSED = True
RIGHT_MOTOR_REVERSED = False

left_in1 = Pin(LEFT_IN1_PIN, Pin.OUT)
left_in2 = Pin(LEFT_IN2_PIN, Pin.OUT)
right_in3 = Pin(RIGHT_IN3_PIN, Pin.OUT)
right_in4 = Pin(RIGHT_IN4_PIN, Pin.OUT)


def _set_motor(pin_a, pin_b, forward, reversed_direction=False):
    if reversed_direction:
        forward = not forward

    pin_a.value(1 if forward else 0)
    pin_b.value(0 if forward else 1)


def _set_left_motor(forward):
    _set_motor(left_in1, left_in2, forward, LEFT_MOTOR_REVERSED)


def _set_right_motor(forward):
    _set_motor(right_in3, right_in4, forward, RIGHT_MOTOR_REVERSED)

# ======== 2. 基础动作封装 ========
def stop():
    """停车：所有控制引脚拉低。"""
    left_in1.value(0)
    left_in2.value(0)
    right_in3.value(0)
    right_in4.value(0)


def forward():
    """前进：左右轮都向前转。"""
    _set_left_motor(True)
    _set_right_motor(True)


def backward():
    """后退：左右轮都向后转。"""
    _set_left_motor(False)
    _set_right_motor(False)


def turn_left():
    """左转：左轮后退，右轮前进。"""
    _set_left_motor(True)
    _set_right_motor(False)


def turn_right():
    """右转：左轮前进，右轮后退。"""
    _set_left_motor(False)
    _set_right_motor(True)


# 文件被导入时，先确保小车处于停止状态。
# stop()