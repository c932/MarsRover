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
import time

TEST_STEP_SECONDS = 1.5
PAUSE_SECONDS = 0.8
RUN_FOREVER = False


def run_step(action_name, action, duration=TEST_STEP_SECONDS):
    """执行一次电机测试动作。"""
    print("开始测试: {}".format(action_name))
    action()
    time.sleep(duration)
    stop()
    print("结束测试: {}".format(action_name))
    time.sleep(PAUSE_SECONDS)


def run_motor_test_cycle():
    """按顺序测试电机动作。"""
    run_step("前进", forward)
    run_step("后退", backward)
    run_step("左转", turn_left)
    run_step("右转", turn_right)
    stop()
    print("本轮测试结束")


print("火星车电机测试程序已启动")
print("将按顺序测试: 前进 -> 后退 -> 左转 -> 右转")
print("如果方向不对，请修改 motor.py 里的动作函数")
print("如果想循环测试，把 RUN_FOREVER 改成 True")

try:
    while True:
        run_motor_test_cycle()
        if not RUN_FOREVER:
            print("测试完成，程序结束")
            break

        print("停车 2 秒后重新开始")
        time.sleep(2)

    stop()

except KeyboardInterrupt:
    stop()
    print("系统手动紧急停机！")
# 文件被导入时，先确保小车处于停止状态。
# stop()