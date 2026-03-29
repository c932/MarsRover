import time
from machine import Pin

class _FallbackMotor:
    def __init__(self):
        self.left_in1 = Pin(0, Pin.OUT)
        self.left_in2 = Pin(1, Pin.OUT)
        self.right_in3 = Pin(2, Pin.OUT)
        self.right_in4 = Pin(3, Pin.OUT)
        self.stop()

    def stop(self):
        self.left_in1.value(0)
        self.left_in2.value(0)
        self.right_in3.value(0)
        self.right_in4.value(0)

    def forward(self):
        self.left_in1.value(1)
        self.left_in2.value(0)
        self.right_in3.value(1)
        self.right_in4.value(0)

    def backward(self):
        self.left_in1.value(0)
        self.left_in2.value(1)
        self.right_in3.value(0)
        self.right_in4.value(1)

    def turn_left(self):
        self.left_in1.value(0)
        self.left_in2.value(1)
        self.right_in3.value(1)
        self.right_in4.value(0)

    def turn_right(self):
        self.left_in1.value(1)
        self.left_in2.value(0)
        self.right_in3.value(0)
        self.right_in4.value(1)


def _resolve_motor():
    required = ("forward", "backward", "turn_left", "turn_right", "stop")

    # 先尝试项目内自定义名称，避免和板载同名模块冲突。
    try:
        import mata as imported_motor
    except ImportError:
        try:
            import motor as imported_motor
        except ImportError:
            print("警告: Pico 上未找到 mata.py，已启用 main.py 内置电机控制。")
            print("建议: 右键执行 Upload project to Pico，再运行 main.py。")
            return _FallbackMotor()

    if all(hasattr(imported_motor, name) for name in required):
        print("已加载电机模块")
        return imported_motor

    print("警告: 检测到电机模块，但缺少必要函数。")
    print("缺少函数时将自动使用内置电机控制，避免程序报错。")
    return _FallbackMotor()


motor = _resolve_motor()

TEST_STEP_SECONDS = 1.5
PAUSE_SECONDS = 0.8
RUN_FOREVER = False


def run_step(action_name, action, duration=TEST_STEP_SECONDS):
    """执行一次电机测试动作。"""
    print("开始测试: {}".format(action_name))
    action()
    time.sleep(duration)
    motor.stop()
    print("结束测试: {}".format(action_name))
    time.sleep(PAUSE_SECONDS)


def run_motor_test_cycle():
    """按顺序测试电机动作。"""
    run_step("前进", motor.forward)
    run_step("后退", motor.backward)
    run_step("左转", motor.turn_left)
    run_step("右转", motor.turn_right)
    motor.stop()
    print("本轮测试结束")


print("火星车电机测试程序已启动")
print("将按顺序测试: 前进 -> 后退 -> 左转 -> 右转")
print("如果方向不对，请修改 mata.py 里的动作函数")
print("如果想循环测试，把 RUN_FOREVER 改成 True")

try:
    while True:
        run_motor_test_cycle()
        if not RUN_FOREVER:
            print("测试完成，程序结束")
            break

        print("停车 2 秒后重新开始")
        time.sleep(2)

    motor.stop()

except KeyboardInterrupt:
    motor.stop()
    print("系统手动紧急停机！")